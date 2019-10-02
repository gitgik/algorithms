""""All the ways to implement a palindrom checker.

A palindrome is defined as a string that is written the same forward and backward.
"""


def is_palindrome1(string):
    """
    Complexity:
        O(n) space
        O(n) time
    """
    reversed_char = []
    for i in reversed(range(len(string))):
        reversed_char.append(string[i])
    return string == "".join(reversed_char)
