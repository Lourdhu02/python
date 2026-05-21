"""
Problem: Merge Two Sorted Lists
Write a function merge_sorted(list1, list2) that merges two sorted
lists into a single sorted list.

Example:
  merge_sorted([1, 3, 5], [2, 4, 6])    # Returns [1, 2, 3, 4, 5, 6]
  merge_sorted([1, 2, 3], [4, 5, 6])   # Returns [1, 2, 3, 4, 5, 6]
  merge_sorted([], [1, 2])              # Returns [1, 2]

Constraints:
  - Both input lists must be sorted
  - Result should also be sorted
  - Can use set() or manual merging
"""


def merge_sorted(list1, list2):
    pass


# Tests
print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]
print(merge_sorted([1, 2, 3], [4, 5, 6]))    # [1, 2, 3, 4, 5, 6]
print(merge_sorted([], [1, 2]))              # [1, 2]
