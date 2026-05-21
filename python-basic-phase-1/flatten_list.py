"""
Problem: Flatten a Nested List
Write a function flatten_list(nested) that takes a nested list
and returns a flat list with all elements.

Example:
  flatten_list([1, [2, 3], [4, [5, 6]]])  # Returns [1, 2, 3, 4, 5, 6]
  flatten_list([[1, 2], [3, 4]])          # Returns [1, 2, 3, 4]
  flatten_list([1, [2], [[3]]])          # Returns [1, 2, 3]

Constraints:
  - Handle multiple levels of nesting
  - Can use recursion or iteration
"""


def flatten_list(nested):
    pass


# Tests
print(flatten_list([1, [2, 3], [4, [5, 6]]]))  # [1, 2, 3, 4, 5, 6]
print(flatten_list([[1, 2], [3, 4]]))          # [1, 2, 3, 4]
print(flatten_list([1, [2], [[3]]]))          # [1, 2, 3]
