"""You are given an array of integers and an integer.
Write a function that moves all the instances of that integer in the array to
the end of the array.

Sample input: [2, 1, 2, 3, 7, 2, 1], 2

Sample output: [1, 3, 7, 1, 2, 2, 2]

"""

def move_elements_to_end(array, to_move):
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == to_move:
            # decrement j to point to an integer that isn't  to_move
            j -= 1

        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]

        # increment i
        i += 1

    return array
