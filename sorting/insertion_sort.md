```python
"""Insertion sort implementation."""


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1,  array)
            j -= 1
    return array


def swap(i, j, array):
    """Swap elements in an array."""
    array[i], array[j] = array[j], array[i]

```


```python
insertion_sort([12, 1, 3, 2, 7, 4, 0])
```




    [0, 1, 2, 3, 4, 7, 12]




```python

```
