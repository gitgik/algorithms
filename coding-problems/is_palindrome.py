""""All the ways to implement a palindrom checker.

Check if the string is a palindrome, return True, otherwise, return False.

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


def is_palindrome_best(string):
    """
    Complexity:
        O(1) space
        O(n) time
    """
    left_index = 0
    right_index = len(string) - 1

    while left_index < right_index:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


def is_palindrome2(string, i = 0):
    """
    Recursive implementation.

    Complexity:
        O(n) space
        O(n) time
    """
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome2(string, i + 1)
