```python
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

def find(board: list, word: str):
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            visited = set()
            if search(board, word, row, col, 0, visited):
                return True
    return False
    
def search(board, word, row, col, index, visited):
    def is_valid(board, row, col):
        return row >= 0 and row <= len(board) and col >= 0 and col <= len(board[0])
    # basecase 1: search is complete without finding
    if not is_valid(board, row, col):
        return False
    if (row, col) in visited:
        return False
    if board[row][col] != word[index]:
        return False
    if index == len(board) - 1:
        return True
    
    visited.add((row, col))
    
    for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if search(board, word, row + d[0], col + d[1], index + 1, visited):
            return True
    # backttrack
    visited.remove((row, col))
    
    return False

```


```python
find(board, "ABCCS")
```




    True




```python
find(board, "ECCE")
```




    True




```python

```
