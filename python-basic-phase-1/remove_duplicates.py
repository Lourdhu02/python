"""
Problem: Remove Duplicates from a List
Write a function remove_duplicates(items) that takes a list
and returns a new list with duplicates removed, preserving original order.

Example:
  remove_duplicates([1, 2, 2, 3, 1, 4, 3])  # Returns [1, 2, 3, 4]
  remove_duplicates(['a', 'b', 'a', 'c'])   # Returns ['a', 'b', 'c']
  remove_duplicates([1, 1, 1])               # Returns [1]

Constraints:
  - Do not use set() to remove duplicates
  - Preserve the order of first occurrences
"""


def remove_duplicates(items):
    pass


# Tests
print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))  # [1, 2, 3, 4]
print(remove_duplicates(['a', 'b', 'a', 'c']))   # ['a', 'b', 'c']
print(remove_duplicates([1, 1, 1]))               # [1]
