"""
Write a function that takes in two strings and returns the minimal number of edit
operations that need to be performed on the first string to get the second string.
Edit Operations include: insertion, deletion and substitition.


Sample input: str1: "abc", str2: "yabd"
Sample output: 2
Explanation: insert "y", substitute: "c" for "d"

"""

def levenshtein_distance(str1, str2):
    """
    Complexity:
        Time: O(nm)
        Space: O(nm), We can use dynamic programming to improve on the space
        complexity.
    """
    edits = [[col for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]
    # [
    #  [0, 1, 2, 3, 4]
    #  [ ... ]
    # ]


    for row in range(1, len(str1) + 1):
    # make the first value of each row to be 1, 2, 3, 4, ...
    # [ [0, 1, 2, ..],
    #   [1, ...]
    #   [2, ...]
    #   [3, ...] ]

        edits[row][0] = edits[row - 1][0] + 1

    # iterate through the 2 dimensional array
    for row in range(1, len(str1) + 1):
        for col in range(1, len(str2) + 1):
            if str1[row - 1] == str2[col - 1]:
                edits[row][col] = edits[row - 1][col - 1]
            else:
                edits[row][col] = 1 + min(
                    edits[row - 1][col],
                    edits[row][col - 1],
                    edits[row - 1][col - 1]
                )

    # return the bottom right value of the two-dim array
    return edits[-1][-1]
