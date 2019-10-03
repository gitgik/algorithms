"""Find the smallest difference between two arrays.

The function should take in two arrays,
Find the pair of numbers in the array whose absolute difference is closest to zero.

"""


def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()

    idx_one = 0
    idx_two = 0

    current_diff = float('inf')
    smallest_diff = float('inf')

    while idx_one < len(array_one) and idx_two < len(array_two):
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]

        if first_num < second_num:
            # increment the index in first array
            current_diff = second_num - first_num
            idx_one += 1

        elif second_num < first_num:
            # increment index in second array
            current_diff = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]

        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [first_num, second_num]

    return smallest_pair
