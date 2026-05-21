"""
Problem: Find Sublist Sum to Target
Write a function find_sublist_sum(numbers, target) that takes a list of
numbers and a target sum. Return the indices of the first two numbers
that add up to the target.

Example:
  find_sublist_sum([2, 7, 11, 15], 9)   # Returns (0, 1) since 2+7=9
  find_sublist_sum([3, 2, 4], 6)        # Returns (1, 2) since 2+4=6
  find_sublist_sum([3, 3], 6)           # Returns (0, 1)

Constraints:
  - Return None if no pair found
  - Each element can only be used once
"""


def find_sublist_sum(numbers, target):
    pass


# Tests
print(find_sublist_sum([2, 7, 11, 15], 9))   # (0, 1)
print(find_sublist_sum([3, 2, 4], 6))        # (1, 2)
print(find_sublist_sum([3, 3], 6))           # (0, 1)
print(find_sublist_sum([1, 2, 3], 10))      # None
