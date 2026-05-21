"""
Problem: Count Word Frequency in a String
Write a function word_frequency(text) that takes a string and returns
a dictionary with each word as key and its count as value.

Example:
  word_frequency("the quick brown fox jumps over the lazy dog")
  # Returns {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
  word_frequency("hello hello hello")  # Returns {'hello': 3}

Constraints:
  - Return lowercase words
  - Handle punctuation
  - Ignore extra spaces
"""


def word_frequency(text):
    pass


# Tests
print(word_frequency("the quick brown fox jumps over the lazy dog"))
print(word_frequency("hello hello hello"))
print(word_frequency("Hello, World! Hello World."))
