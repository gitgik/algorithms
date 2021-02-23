### Longest Peak
Write a function that takes in an array and returns the length of the longest peak in the array.

A peak is defined as adjacent elements that are strictly increasing towards a peak tip, then scrictly decreasing.

For instance, the array values `1, 2, 5, 3, 0` have a peak, while `10, 0, 4`. Similarly, `1, 2, 3` isn't a peak beacuase there aren't any integers decreasing after 3.

Note: There can exist more than one peak in the array. Return the longest one.

Sample input:
```
[11, 3, 6, 4, 0, 10, 6, 5, -3, -1, 10]
```

Sample output:
```
6
```


```python
def longest_peak(A):
    """
    Complexity: O(1) space,  O(n) time, where n is the total number of elements in the array A.
    """
    
    longest_peak_length = 0
    # start from the second elem in array (i = 1)
    i = 1
    while i < len(A) - 1:
        # check each element for peakness
        peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not peak:
            i += 1
            continue
        # spread outwards in left direction to find peak start.
        left_index = i - 2
        while left_index >= 0 and A[left_index] < A[left_index + 1]:
            left_index -= 1
        # spread outwards in right direction to find peak stop.
        right_index = i + 2
        while right_index < len(A) and A[right_index] < A[right_index - 1]:
            right_index += 1

        current_peak_length = right_index - left_index - 1
        longest_peak_length = max(current_peak_length, longest_peak_length)
        i = right_index
    return longest_peak_length
```


```python
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
longest_peak(array)
```




    6


