"""
Problem: Find Common Elements in Two Lists
Write a function common_elements(list1, list2) that returns a list
containing elements that appear in both lists.

Example:
  common_elements([1, 2, 3, 4], [3, 4, 5, 6])  # Returns [3, 4]
  common_elements(['a', 'b', 'c'], ['b', 'c', 'd'])  # Returns ['b', 'c']

Constraints:
  - Preserve the order from first list
  - Each common element appears only once in result
"""


def common_elements(list1, list2):
    pass


# Tests
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))           # [3, 4]
print(common_elements(['a', 'b', 'c'], ['b', 'c', 'd']))      # ['b', 'c']
print(common_elements([1, 2, 3], [4, 5, 6]))                 # []
