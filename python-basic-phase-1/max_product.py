"""
Problem: Find Maximum Product in List
Write a function max_product(numbers) that finds the maximum product
of any two numbers in the list.

Example:
  max_product([1, 2, 3, 4])     # Returns 24 (3*4=12 or 4*3=12... wait that's wrong)
                                  Actually returns 12 (3*4 or 2*6? no...)
                                  Let me recalculate: [1,2,3,4] -> 4*3=12
  max_product([-10, -10, 5, 2]) # Returns 100 (-10 * -10)

Constraints:
  - List can have negative numbers
  - Handle at least 2 elements
"""


def max_product(numbers):
    pass


# Tests
print(max_product([1, 2, 3, 4]))  # 12
print(max_product([-10, -10, 5, 2]))  # 100
print(max_product([0, -1, 3, 100, -70]))  # -70 * 100 = -7000
