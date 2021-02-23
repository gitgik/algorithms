### Spiral Traverse
Write a function that takes in an n X m two-dimensional array and returns an array of the elements in spiral order.

For instance, given
```
[
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
```
The function should return 
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

#### Iterative solution


```python

def spiral_traverse(A):
    """Complexity analysis:
        O(n) time, O(n) space, where n is the total number of elements in the 2-dimensional array
    """
    # first define starting and ending row, starting and ending column
    start_row, end_row = 0, len(A) - 1
    start_col, end_col = 0, len(A[0]) - 1
    
    output = []
    while start_row <= end_row and start_col <= end_col:
        
        for col in range(start_col, end_col + 1):
            output.append(A[start_row][col])
        
        for row in range(start_row + 1, end_row + 1):
            output.append(A[row][end_col])
        
        for col in reversed(range(start_col, end_col)):
            # prevent double counting of the row (in case we have counted it in for-loop 1)
            if start_row == end_row:
                break
            output.append(A[end_row][col])
        
        for row in reversed(range(start_row + 1, end_row)):
            # prevent double counting of column (in case we have counted it in for loop 2)
            if start_col == end_col:
                break
            output.append(A[row][start_col])
        
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1

    return output
```


```python
A = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
spiral_traverse(A)
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]



#### Recursive solution


```python
def spiral_traversal(array):
    """Complexity analysis:
        O(n) time, O(n) space, where n is the total number of elements in the array.
    """
    output = []
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, output)
    return output

def spiral_fill(A, start_row, end_row, start_col, end_col, output):
    
    if start_row > end_row or start_col > end_col:
        return
    
    for col in range(start_col, end_col + 1):
        output.append(A[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        output.append(A[row][end_col])

    for col in reversed(range(start_col, end_col)):
        # prevent double counting of the row (in case we have counted it in for-loop 1)
        if start_row == end_row:
            break
        output.append(A[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        # prevent double counting of column (in case we have counted it in for loop 2)
        if start_col == end_col:
            break
        output.append(A[row][start_col])

    return spiral_fill(A, start_row + 1, end_row - 1, start_col + 1, end_col - 1, output)
```


```python
B = [
    [2, 4, 6, 8],
    [32, 34, 36, 10],
    [30, 48, 38, 12],
    [28, 46, 40, 14],
    [26, 44, 42, 16],
    [24, 22, 20, 18]
]
spiral_traverse(B)
```




    [2,
     4,
     6,
     8,
     10,
     12,
     14,
     16,
     18,
     20,
     22,
     24,
     26,
     28,
     30,
     32,
     34,
     36,
     38,
     40,
     42,
     44,
     46,
     48]




```python

```
