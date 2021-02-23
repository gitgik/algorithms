### Problem
Write a function that takes in a two-dim array and returns all the elemets in the array in a one-dimensional array after traversing in a zigzag order.

Sample input:
array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16],
]

Sample output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


```python
# O(n) time | O(n) space
def zigzagTraverse(array):
    row, col = 0, 0
    width = len(array[0]) - 1
    height = len(array) - 1
    results = []
    going_down = True
    
    while not is_out_of_bounds(row, col, height, width):
        results.append(array[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                # go down
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                # climb up
                row -= 1
                col += 1
    return results

def is_out_of_bounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
```


```python
array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16],
]
zigzagTraverse(array)
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]




```python

```
