"""
update_progress.py
------------------
Run this script before every git push.
It scans all phase folders, reads file timestamps, and auto-updates:
  - README.md        (progress badge)
  - PROGRESS.md      (full detailed log)
  - CHANGELOG.md     (daily activity log)
"""

import os
import re
from datetime import datetime, date
from pathlib import Path
from collections import defaultdict

# ── Config ────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent

PHASES = [
    {"folder": "python-basic-phase-1",       "name": "Phase 1 — Python Basics",              "days": "001–073"},
    {"folder": "python-intermediat-phase-2",  "name": "Phase 2 — Intermediate Python",         "days": "074–146"},
    {"folder": "python-advance-phase-3",      "name": "Phase 3 — Advanced Python",             "days": "147–219"},
    {"folder": "python-dsa-phase-4",          "name": "Phase 4 — Data Structures & Algorithms","days": "220–292"},
    {"folder": "python-core",                 "name": "Phase 5 — Python Core & Internals",     "days": "293–365"},
]

TOTAL_DAYS = 365

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_files(folder: Path) -> list[dict]:
    """Return sorted list of .py files with metadata."""
    files = []
    if not folder.exists():
        return files
    for f in sorted(folder.glob("*.py")):
        ts = f.stat().st_mtime
        added = datetime.fromtimestamp(ts)
        files.append({
            "name": f.name,
            "path": f,
            "date": added.date(),
            "datetime": added,
        })
    return files


def calc_streak(all_dates: list[date]) -> int:
    """Calculate current consecutive-day streak from today backwards."""
    if not all_dates:
        return 0
    unique = sorted(set(all_dates), reverse=True)
    today = date.today()
    streak = 0
    expected = today
    for d in unique:
        if d == expected:
            streak += 1
            expected = date.fromordinal(expected.toordinal() - 1)
        elif d < expected:
            break
    return streak


def update_badge(readme_path: Path, completed: int, total: int):
    """Update the progress badge count in README.md."""
    if not readme_path.exists():
        print("  [skip] README.md not found")
        return
    content = readme_path.read_text(encoding="utf-8")
    new_badge = f"Progress-{completed}%20%2F%20{total}%20Days"
    updated = re.sub(r"Progress-\d+%20%2F%20\d+%20Days", new_badge, content)
    if updated != content:
        readme_path.write_text(updated, encoding="utf-8")
        print(f"  [updated] README.md badge -> {completed}/{total}")
    else:
        print(f"  [no change] README.md badge already at {completed}/{total}")


# ── PROGRESS.md ───────────────────────────────────────────────────────────────

def build_progress_md(phase_data: list[dict], streak: int, total_completed: int) -> str:
    today = date.today().strftime("%B %d, %Y")
    lines = []

    lines.append("# Progress Log\n")
    lines.append(f"**Last updated:** {today}\n")
    lines.append("")

    # Summary
    lines.append("## Summary\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total Completed | {total_completed} / {TOTAL_DAYS} |")
    lines.append(f"| Current Streak | {streak} day{'s' if streak != 1 else ''} |")
    lines.append(f"| Phases Active | {sum(1 for p in phase_data if p['files'])} / {len(PHASES)} |")
    lines.append(f"| Last Activity | {max((f['date'] for p in phase_data for f in p['files']), default='—')} |")
    lines.append("")

    # Phase breakdown
    lines.append("## Phase Breakdown\n")
    lines.append("| Phase | Folder | Completed | Days |")
    lines.append("|-------|--------|-----------|------|")
    for p in phase_data:
        count = len(p["files"])
        status = "In Progress" if count > 0 else "Not Started"
        lines.append(f"| {p['name']} | `{p['folder']}` | {count} | {p['days']} |")
    lines.append("")

    # Per-phase problem tables
    lines.append("## Problems by Phase\n")
    for p in phase_data:
        lines.append(f"### {p['name']}\n")
        lines.append(f"`{p['folder']}/` &nbsp;·&nbsp; Days {p['days']}\n")
        if not p["files"]:
            lines.append("No solutions added yet.\n")
            continue
        lines.append("| # | File | Date Added |")
        lines.append("|---|------|------------|")
        for i, f in enumerate(p["files"], 1):
            lines.append(f"| {i:03d} | `{f['name']}` | {f['date']} |")
        lines.append("")

    return "\n".join(lines)


# ── CHANGELOG.md ──────────────────────────────────────────────────────────────

def build_changelog_md(phase_data: list[dict]) -> str:
    # Group all files by date
    by_date = defaultdict(list)
    for p in phase_data:
        for f in p["files"]:
            by_date[f["date"]].append({
                "file": f["name"],
                "phase": p["name"],
                "folder": p["folder"],
            })

    lines = []
    lines.append("# Changelog\n")
    lines.append("Daily activity log — auto-generated by `update_progress.py`.\n")
    lines.append("")

    for d in sorted(by_date.keys(), reverse=True):
        lines.append(f"## {d.strftime('%B %d, %Y')}\n")
        for entry in by_date[d]:
            lines.append(f"- `{entry['file']}` — {entry['phase']}")
        lines.append("")

    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("\n=== update_progress.py ===\n")

    # Collect data from all phases
    phase_data = []
    all_dates = []

    for phase in PHASES:
        folder = BASE_DIR / phase["folder"]
        files = get_files(folder)
        all_dates.extend(f["date"] for f in files)
        phase_data.append({
            **phase,
            "files": files,
        })
        print(f"  {phase['folder']:<40} {len(files)} file(s)")

    total_completed = sum(len(p["files"]) for p in phase_data)
    streak = calc_streak(all_dates)

    print(f"\n  Total completed : {total_completed} / {TOTAL_DAYS}")
    print(f"  Current streak  : {streak} day(s)\n")

    # Update README.md badge
    print("Updating README.md...")
    update_badge(BASE_DIR / "README.md", total_completed, TOTAL_DAYS)

    # Write PROGRESS.md
    print("Writing PROGRESS.md...")
    progress_md = build_progress_md(phase_data, streak, total_completed)
    (BASE_DIR / "PROGRESS.md").write_text(progress_md, encoding="utf-8")
    print("  [done] PROGRESS.md")

    # Write CHANGELOG.md
    print("Writing CHANGELOG.md...")
    changelog_md = build_changelog_md(phase_data)
    (BASE_DIR / "CHANGELOG.md").write_text(changelog_md, encoding="utf-8")
    print("  [done] CHANGELOG.md")

    print("\nAll done. Review the files, then:\n")
    print("  git add .")
    print(f"  git commit -m \"Day {total_completed:03d} | Phase X | Your Topic\"")
    print("  git push origin main\n")


if __name__ == "__main__":
    main()
