```python
"""
Implementation of bubble sort.

Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output [2, 3, 5, 5, 6, 8, 9 ]
"""


def bubble_sort(array):
    """
    Sort the list by swapping adjacent elements.

    Complexity:
        O(1) space
        O(n^2) time
    """
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

```


```python
bubble_sort([8, 5, 2, 9, 5, 6, 3])
```




    [2, 3, 5, 5, 6, 8, 9]




```python

```
