"""
Write a function that takes in an array of integers of at least length 2.
Find the smallest sub array in the input array that should be sorted in order for the
entire input array to be sorted.
The function should return an array of the first index and last index
of the smallest sub-array.

If  the whole input array is already sorted, return [-1, -1]

Sample input: [1, 2, 4, 10, 15, 3, 5, 7, 17]
Sample output: [2, 7]
"""


def sub_array_sort(array):
    """Complexity: O(n) time | O(1) space."""

    min_unsorted_num = float('inf')
    max_unsorted_num = float('-inf')

    for i in range(len(array)):
        num = array[i]

        if is_out_of_order(i, num,  array):
            min_unsorted_num = min(max_unsorted_num, num)
            max_unsorted_num = max(max_unsorted_num, num)

    if min_unsorted_num == float('inf'):
        return [-1, -1]

    min_index = 0
    max_index = len(array - 1)

    while min_unsorted_num >= array[min_index]:
        min_index += 1

    while max_unsorted_num <= array[max_index]:
        max_index -= 1

    return [min_index, max_index]


def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]

    if i == len(array) - 1:
        return num < array[i - 1]

    return num > array[i + 1] or num < array[i - 1]
