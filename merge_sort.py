"""Merge sort implementation."""


def merge_sort(array):
    if len(array) <= 1:
        # already sorted
        return array

    middle = len(array) // 2
    # split array into smaller arrays
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left_array, right_array):
    result = []
    left_index = 0
    right_index = 0

    while len(result) < (len(right_array) + len(left_array)):
        if left_array[left_index] <= right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1
        else:
            result.append(right_array[right_index])
            right_index += 1

        # if we are at the end of either of the lists,
        if left_index == len(left_array):
            # reached the end of left list, append the remainder of right list
            result += right_array[right_index:]
            break
        elif right_index == len(right_array):
            # reached the end of right list, append the remainder of left list
            result += left_array[left_index:]
            break
    return result
