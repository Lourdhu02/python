"""
Problem: Check if String Contains Unique Characters
Write a function has_unique_chars(text) that returns True if the string
contains all unique characters (no duplicates), False otherwise.

Example:
  has_unique_chars("abcdef")    # Returns True
  has_unique_chars("hello")     # Returns False
  has_unique_chars("")          # Returns True

Constraints:
  - Case sensitive ('a' and 'A' are different)
  - Handle empty string
  - Do not use set() directly for checking
"""


def has_unique_chars(text):
    pass


# Tests
print(has_unique_chars("abcdef"))  # True
print(has_unique_chars("hello"))   # False
print(has_unique_chars(""))        # True
print(has_unique_chars("aA"))      # True
