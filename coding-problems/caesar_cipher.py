"""Caecar Cipher implementation.

Given a non-empty string of lowercase alphabetic characters, write a function that
takes in the string, and an integer called a key,
And returns a string obtained by shifting every letter of the input string by k positions
in the alphabet, where k is the key.

Sample input: "xyz", 2
Sample output: "zab"
"""


def caesar_cipher_encryptor(string, key):
    """
    Complexity:
        O(n) space
        O(n) time
    """
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letter_code = ord(letter) + new_key
        if new_letter_code > 122:  # z character code is 122
            character = chr(96 + new_letter_code % 122)
            new_letters.append(character)
        else:
            new_letters.append(chr(new_letter_code))

    return "".join(new_letters)
