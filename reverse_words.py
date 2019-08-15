def reverse(li, start, end):
    """Reverse characters in a string from start to end(inclusive)."""
    while start < end:
        li[start], li[end] = li[end], li[start]

        start += 1
        end -= 1


def reverse_mutable_string(string_list):
    """
    This function performs a reverse operation on a mutable string in-place.
    (saving on space)
    Since strings are immutable, a mutable string can be represented
    as a list of characters in a buffer e.g
    ['h','e','l','l','o',' ','w','o','r','l','d']) == 'hello world'

    Approach: First, we reverse entire string to get 'dlrow olleh',
    then we reverse each word withing string to obtain original words.

    Worst-case omplexity:
        Time: O(n)
        Space: O(1) - since the input memory location is overwritten by the
        output as we reverse the string as the algorithm executes.
    """
    # reverse entire string
    reverse(string_list, 0, len(string_list) - 1)

    print('Reversing entire string:\n', string_list)

    # reverse each word in the string
    start = 0
    for end in range(len(string_list)):
        if string_list[end] == " ":
            print(f'reversing a word from index:{start} to {end - 1}')
            reverse(string_list, start, end - 1)
            start = end + 1

    # reverse last word since we stopped at the last white space in the list
    # remember, there are characters after the white space.
    print(f'reversing last word from index:{start} to {len(string_list) - 1}')
    reverse(string_list, start, len(string_list) - 1)
    return string_list


# test it
mutable_string = list("well hello there")
reverse_mutable_string(mutable_string)
