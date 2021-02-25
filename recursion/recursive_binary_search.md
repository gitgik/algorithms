### Binary search recursive approach


```python
def binary_search(A, value):
    if len(A) == 0:
        return -1
    return binary_search_helper(A, 0, len(A) - 1, value)

def binary_search_helper(A, left, right, value):
    # base case
    if left > right:
        return -1
    mid = (right + left) // 2
    if A[mid] == value:
        return mid
    elif A[mid] > value:
        return binary_search_helper(A, left, mid, value)
    elif A[mid] < value:
        return binary_search_helper(A, mid + 1, right, value)
```


```python
A = [1, 2, 3]
binary_search(A, 13)
```




    -1




```python
array = [1, 2, 3, 5, 7, 13, 14, 16]
binary_search(array, 7)
```




    4




```python

```
