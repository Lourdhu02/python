# Git Workflow & Commit Convention

## Daily Workflow

```bash
# 1. Write your solution in the correct phase folder
# 2. Stage it
git add python-basic-phase-1/your_file.py

# 3. Commit with the standard message format
git commit -m "Day 015 | Phase 1 | Fibonacci Sequence"

# 4. Push
git push origin main
```

---

## Commit Message Format

```
Day <NNN> | Phase <N> | <Topic>
```

**Examples:**

```
Day 015 | Phase 1 | Fibonacci Sequence
Day 016 | Phase 1 | Palindrome Check
Day 101 | Phase 2 | OOP — Bank Account class
Day 201 | Phase 3 | Decorator Pattern
Day 301 | Phase 4 | Binary Search
Day 365 | Phase 4 | Final Day — Graph BFS
```

**Optional tag prefix for clarity:**

| Tag | Use |
|-----|-----|
| `[add]` | New solution — `Day 015 | Phase 1 | [add] Fibonacci` |
| `[fix]` | Bug fixed |
| `[refactor]` | Code refactored |
| `[notes]` | Comments or notes updated |

---

## Phase to Folder Mapping

| Phase | Folder | Days |
|-------|--------|------|
| 1 | `python-basic-phase-1/` | 001–073 |
| 2 | `python-intermediat-phase-2/` | 074–146 |
| 3 | `python-advance-phase-3/` | 147–219 |
| 4 | `python-dsa-phase-4/` | 220–292 |
| 5 | `python-core-phase-5/` | 293–365 |

---

## Useful Commands

```bash
# View commit history in one line
git log --oneline

# View history with graph
git log --oneline --graph --all

# Undo last commit but keep your files
git reset --soft HEAD~1

# Tag a completed phase
git tag -a "phase-1-complete" -m "Completed Phase 1 — Python Basics"
git push origin --tags
```