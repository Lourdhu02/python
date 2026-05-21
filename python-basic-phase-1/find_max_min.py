"""
Problem: Find Maximum and Minimum in a List
Write a function find_max_min(numbers) that takes a list of numbers
and returns both the maximum and minimum values as a tuple (max, min).

Example:
  find_max_min([3, 1, 4, 1, 5, 9, 2, 6])  # Returns (9, 1)
  find_max_min([10])                      # Returns (10, 10)
  find_max_min([-5, 0, 5])                # Returns (5, -5)

Constraints:
  - Use only basic loops (no max() or min() built-in)
  - Handle empty list case (return None or raise error)
"""


def find_max_min(numbers):
    pass


# Tests
print(find_max_min([3, 1, 4, 1, 5, 9, 2, 6]))  # (9, 1)
print(find_max_min([10]))                      # (10, 10)
print(find_max_min([-5, 0, 5]))                 # (5, -5)
print(find_max_min([]))                        # None
