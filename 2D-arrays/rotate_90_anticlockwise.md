## Rotate a matrix -90 degrees

Given a 2 dimensional array, rotate it 90 degrees anti-clockwise in constant space.

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
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7],
]
```


```python
def rotate_anti_90(matrix):
    # first, transpose the matrix, swaping i and j (the elements in the diagonal won't move)
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # IF matrix = [
    #   [1, 2, 3],
    #   [4, 5, 6],
    #   [7, 8, 9]
    # ] 
    # Then matrix currently looks like this
    #  [
    #   [1, 4, 7]
    #   [2, 5, 8]
    #   [3, 6, 9]
    # ]
    
    
    # For each column (j) in the matrix, swap the top (i) with the bottom (ith) element. 
    # Work inwards, withing the inner for loop and swap accordingly. 
    # For a matrix that has an odd length, the inner element won't be swapped. 
    for j in range(m):
        for i in range(n // 2):
            # swapping
            A[i][j], A[n - 1 - i][j] = A[n - 1 - i][j], A[i][j]

    return A
```


```python
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_anti_90(A)
```




    [[3, 6, 9], [2, 5, 8], [1, 4, 7]]


