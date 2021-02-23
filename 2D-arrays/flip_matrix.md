## Problem
Given a matrix, flip it in constant space, and without using in-built methods.

For example given
```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
```

Return 

```python
[
    [4, 3, 2, 1], 
    [8, 7, 6, 5], 
    [12, 11, 10, 9], 
    [16, 15, 14, 13]
]
```



```python
def flip_matrix(matrix):
    n, m = len(matrix), len(matrix[0]) 
    for i in range(n):
        for j in range(m // 2):
            matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]
    return matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

flip_matrix(matrix)
```




    [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]


