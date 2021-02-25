### Given an array of unsorted integers, sort it using selection sort.


```python

def find_smallest(A):
    smallest = A[0]
    smallest_index = 0
    for i in range(1, len(A)):
        if A[i] < smallest:
            smallest = A[i]
            smallest_index = i
    return smallest_index

def selection_sort(A):
    """Complexity: O(n^2) time | O(n) space (Although we can achieve constant time if we sort inplace)"""
    sorted_array = []
    for i in range(len(A)):
        smallest_index = find_smallest(A)
        sorted_array.append(A.pop(smallest_index))
    return sorted_array

```


```python
A = [1, 2, 3, -2, 0, 5]
selection_sort(A)
```




    [-2, 0, 1, 2, 3, 5]


