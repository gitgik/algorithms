## Problem

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

```python
matrix = [
    [1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1]
]
 ```
Return 6




```python
from typing import List

def largest_rectangle(matrix: List[List[int]]) -> int:
    """O(M^3 * N^3) time | O(1) space"""
    
    max_so_far = 0
    n, m = len(matrix), len(matrix[0])
    for top_left_row in range(n):
        for top_left_col in range(m):
            for bottom_right_row in range(n, top_left_row, -1):
                for bottom_right_col in range(m, top_left_col, -1):
                    # check if the cell is valid (has 1)
                    if is_valid(
                        matrix,
                        top_left_row,
                        top_left_col,
                        bottom_right_row,
                        bottom_right_col
                    ):
                        max_so_far = max(
                            max_so_far, 
                            ((bottom_right_row - top_left_row) * (bottom_right_col - top_left_col))
                        )
    return max_so_far


def is_valid(matrix, top_left_row, top_left_col, bottom_right_row, bottom_right_col):
    for i in range(top_left_row, bottom_right_row):
        for j in range(top_left_col, bottom_right_col):
            if matrix[i][j] == 0:
                return False
    return True
```


```python
matrix = [
    [1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1]
]
largest_rectangle(matrix)
```




    6




```python

```
