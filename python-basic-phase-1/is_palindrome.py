"""
Problem: Palindrome Check
Write a function is_palindrome(text) that returns True if the given
string or number is a palindrome, False otherwise.

Example:
  is_palindrome("racecar")      # Returns True
  is_palindrome("hello")        # Returns False
  is_palindrome(12321)          # Returns True
  is_palindrome("A man a plan a canal Panama")  # Returns True

Constraints:
  - Ignore spaces and punctuation for strings
  - Case insensitive
"""


def is_palindrome(text):
    test = str(text).replace(" ", "").lower()
    if test == test[::-1]:
        return True
    else:
        return False


# Tests
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome(12321))  # True
print(is_palindrome("A man a plan a canal Panama"))  # True
