### Rotate a matrix 90 degrees
Given a 2 dimensional array, rotate it 90 degrees clockwise in constant space.

Sample input:
```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

Sample output:
```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
```


```python
"""
The solution is a two-parter:
We'll do an in-place rearrangement of the elements in the array, swapping them to become a 90 degree rotation.
1. Transpose our matrix: taking our rows and turn them into columns... we'll loop through the array and swap(a[i][j], a[j][i]). Note: the diagonal won't get swapped.
2. Flip horizontally: we'll have two pointers moving towards the center, left([i][j] -->, <---[i][n-1-j] right. We'll then swap the elements on their path. 
If the middle elements are odd, they won't be swapped. 
"""

def rotate_90(array):
    for i in range(0, len(array)):
        for j in range(i, len(array[0])):
            array[i][j], array[j][i] = array[j][i], array[i][j]

    n = len(array)
    for i in range(0, n):
        for j in range(0, n // 2):
            array[i][j], array[i][n - 1 - j] = array[i][n - 1 - j], array[i][j]
            
    return array
```


```python
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate_90(array)
```




    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]




```python

```


```python

```
