"""
Write a function that takes in an array of ints,
returns a sorted array of three largest
integers from the array.
Note that the function should return duplicate integers if necessary;
e.g: it should return [10, 10, 12] for an input array [10, 5, 9, 10, 12, 7]

Sample input: [141, 1, 16, -7, -17, -20, 18, 541, 8, 7, 7]
"""


def find_three_largest_numbers(array):
    """Find the three largest integers from a list of integers.

    Complexity:
        O(n) time, since we traverse the n-length list to the end
        O(1) space, because we only store the final array of the 3 largest numbers
    """
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)

    return three_largest


def update_largest(three_largest, number):
    if three_largest[2] is None or number > three_largest[2]:
        # update the third largets number
        shift_and_update(three_largest, number, 2)
    elif three_largest[1] is None or number > three_largest[1]:
        shift_and_update(three_largest, number, 1)
    elif three_largest[0] is None or number > three_largest[0]:
        shift_and_update(three_largest, number, 0)


def shift_and_update(array, number,  index):
    for i in range(index + 1):
        if i == index:
            array[i] = number
        else:
            array[i] = array[i + 1]
