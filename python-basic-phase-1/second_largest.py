"""
Problem: Find the Second Largest Number
Write a function second_largest(numbers) that takes a list of numbers
and returns the second largest number.

Example:
  second_largest([10, 5, 8, 3, 15, 12])  # Returns 12
  second_largest([5, 5, 5])               # Returns None
  second_largest([1, 2])                 # Returns 2

Constraints:
  - Do not use sorted() or built-in max/min
  - Handle duplicates properly
  - Return None if no second largest exists
"""


def second_largest(numbers):
    pass


# Tests
print(second_largest([10, 5, 8, 3, 15, 12]))  # 12
print(second_largest([5, 5, 5]))               # None
print(second_largest([1, 2]))                   # 2
print(second_largest([15, 15, 12, 10]))        # 12
