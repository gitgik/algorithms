def binary_search(array, target):
    """
    A function that takes in a sorted array of integers
    and a target integer. It uses the binary search algorithm to find if the target
    number is contained in the array, returning its index if it is, or -1 if it isn't.

    Complexity:
        O(log n) time - because we are splitting the array by half every time
                        we shift the left or right indexes.
        O(1) space
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1
