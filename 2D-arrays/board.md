## Find Word in 2D Board

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

```python
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

exists(board, "ABCCED") returns true, 

exists(board, "SEE") returns true, 

exists(board, "ABCB") returns false.

### Approach
We can view the board as a graph, where the characters are nodes, and their edges point to adjacent characters. We can then perform a depth-first or breadth-first search. 

We can choose DFS because it is easier to implement.

The recursive depth will be limited by the length.
Since we can exit the search once we reach the end of the word, the recursive depth of the call stack will be limited by the length of the word.


```python
def search(board, row, col, word, index, visited):
    def is_valid(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
    
    if not is_valid(board, row, col):
        return False
    if (row, col) in visited:
        return False
    if board[row][col] != word[index]:
        return False
    if index == len(word) - 1:
        return True
    
    print(f'Adding {(row, col)} into set')
    visited.add((row, col))
    
    for d in  ((0, -1), (0, 1), (-1, 0), (1, 0)):
        print(f"searching at {(row + d[0], col + d[1])}")
        
        if search(board, row + d[0], col + d[1], word, index + 1, visited):
            return True
    # backtrack
    print(f"removing {(row, col)} from set")
    visited.remove((row, col))  
    
    return False
    
    
def find_word(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            visited = set()
            if search(board, row, col, word, 0, visited):
                return True
    return False
```


```python
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

find_word(board, 'SEE')
```

    Adding (1, 0) into set
    searching at (1, -1)
    searching at (1, 1)
    searching at (0, 0)
    searching at (2, 0)
    removing (1, 0) from set
    Adding (1, 3) into set
    searching at (1, 2)
    searching at (1, 4)
    searching at (0, 3)
    Adding (0, 3) into set
    searching at (0, 2)
    searching at (0, 4)
    searching at (-1, 3)
    searching at (1, 3)
    removing (0, 3) from set
    searching at (2, 3)
    Adding (2, 3) into set
    searching at (2, 2)





    True




```python
find_word(board, 'AWORD')
```

    Adding (0, 0) into set
    searching at (0, -1)
    searching at (0, 1)
    searching at (-1, 0)
    searching at (1, 0)
    removing (0, 0) from set
    Adding (2, 0) into set
    searching at (2, -1)
    searching at (2, 1)
    searching at (1, 0)
    searching at (3, 0)
    removing (2, 0) from set





    False




```python

```
