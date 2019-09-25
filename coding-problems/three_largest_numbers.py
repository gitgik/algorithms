def find_three_largest_numbers(array):
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
