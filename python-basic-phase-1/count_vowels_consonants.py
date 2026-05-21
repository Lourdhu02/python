"""
Problem: Count Vowels and Consonants in a String
Write a function count_vowels_consonants(text) that takes a string
and returns a dictionary {'vowels': count, 'consonants': count}.

Example:
  count_vowels_consonants("hello")     # Returns {'vowels': 2, 'consonants': 3}
  count_vowels_consonants("AEIOU")     # Returns {'vowels': 5, 'consonants': 0}
  count_vowels_consonants("12345")     # Returns {'vowels': 0, 'consonants': 0}

Constraints:
  - Case insensitive
  - Consider only alphabetic characters
"""


def count_vowels_consonants(text):
    pass


# Tests
print(count_vowels_consonants("hello"))     # {'vowels': 2, 'consonants': 3}
print(count_vowels_consonants("AEIOU"))     # {'vowels': 5, 'consonants': 0}
print(count_vowels_consonants("12345"))     # {'vowels': 0, 'consonants': 0}
print(count_vowels_consonants("Hello World")) # {'vowels': 3, 'consonants': 7}
