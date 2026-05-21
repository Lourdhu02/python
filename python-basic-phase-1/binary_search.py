"""
Problem: Binary Search
Write a function binary_search(numbers, target) that implements binary
search to find if target exists in a sorted list.

Example:
  binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)  # Returns True (index 4)
  binary_search([1, 2, 3, 4, 5], 10)             # Returns False

Constraints:
  - List must be sorted
  - Return True/False, optionally with index
  - Implement binary search algorithm manually
"""


def binary_search(numbers, target):
    pass


# Tests
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # True
print(binary_search([1, 2, 3, 4, 5], 10))  # False
print(binary_search([1], 1))  # True
