"""
Problem: Caesar Cipher
Write a function caesar_cipher(text, shift) that encodes a string
using Caesar Cipher with the given shift.

Example:
  caesar_cipher("ABC", 2)    # Returns "CDE"
  caesar_cipher("xyz", 3)    # Returns "ABC"
  caesar_cipher("Hello", 1)  # Returns "Ifmmp"

Constraints:
  - Handle wrapping from Z to A
  - Case insensitive (preserve case)
  - Only shift alphabetic characters
"""


def caesar_cipher(text, shift):
    pass


# Tests
print(caesar_cipher("ABC", 2))    # CDE
print(caesar_cipher("xyz", 3))    # ABC
print(caesar_cipher("Hello", 1))  # Ifmmp
