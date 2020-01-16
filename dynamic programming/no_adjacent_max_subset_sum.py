"""
Write a function that takes in an array of positive integers, and returns an integer
representing the maximum sum of non-adjacent elements in the array.
If a sum can't be generated, return 0

Sample input: [7, 10, 12, 8, 9, 15]
Sample output: 34 -> [7 + 12 + 15]

"""


def max_subset_no_adjacent_sum(array):
    """
    Complexity:
        Space: O(n)
        Time: O(n)
    """
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    max_sum = array[:]

    max_sum[1] = max(max_sum[0], max_sum[1])

    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + array[i])

    return max_sum[-1]
