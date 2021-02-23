## Problem
Find the smallest difference between two arrays.

The function should take in two arrays and find the pair of numbers in the array whose absolute difference is closest to zero.



```python
def smallest_difference(array_one, array_two):
    """
    Complexity:
        Time: O(nlog(n))  +  mlog(m))
        where n = length of first array, m = length of second array
        (the nlog n comes from sorting using an optimal sorting algorithm)

        Space: O(1)
    """

    # first, we sort the arrays
    array_one.sort()
    array_two.sort()

    # init pointers that we'll use for each array
    idx_one = 0
    idx_two = 0

    current_diff = float('inf')
    smallest_diff = float('inf')

    while idx_one < len(array_one) and idx_two < len(array_two):
        first_num = array_one[idx_one]
        second_num = array_two[idx_two]

        # find absolute difference
        current_diff = abs(first_num - second_num)

        if first_num < second_num:
            # increment the index of first array
            idx_one += 1
        elif second_num < first_num:
            # increment the index of second array
            idx_two += 1
        else:
            return [first_num, second_num]

        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [first_num, second_num]

    return smallest_pair

```


```python
array1 = [2, 1, 3, 5, 4]
array2 = [4, 5, 6, 3, 2]
smallest_difference(array1, array2)
```




    [2, 2]




```python

```
