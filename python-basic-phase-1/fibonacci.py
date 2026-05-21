"""
Problem: Fibonacci Sequence
Write a function fibonacci(n) that returns the nth number in the
Fibonacci sequence.

Example:
  fibonacci(0)    # Returns 0
  fibonacci(1)    # Returns 1
  fibonacci(6)    # Returns 8 (0, 1, 1, 2, 3, 5, 8)
  fibonacci(10)   # Returns 55

Constraints:
  - Handle n=0 and n=1 as base cases
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Tests
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8
print(fibonacci(10))  # 55
