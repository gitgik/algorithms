### Boggle Board
Given a two-dim array containing letters; and representing a boggle board, write a function that returns an array of all words contained in the boggle board.

&nbsp;

A word is constructed in the boggle board by connecting adjacent letters (horizontal, vertical, diagonal), without using any single letter at any given position more than once. While a word can have repeated letters, those repeated letters must be obtained from different positions in the board. Two or more words are allowed to share any give letter in the board.

Sample input:
```python
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
]

words = [
    'this', 'is', 'a', 'simple', 'boggle', 'board', 'REPEATED', 'test', 'not', 'NOTRE-PEATED'
]
```
Sample output:
```python
['this', 'is', 'simple', 'a', 'boggle', 'board', 'NOTRE-PEATED']
```



```python
board = [
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
  ["x", "x", "x", "x", "x", "x", "x"],
  ["N", "O", "T", "R", "E", "-", "P"],
  ["x", "x", "D", "E", "T", "A", "E"]
]
```


```python
# get the neighbors
def getNeighbors(i, j, board):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    if i > 0:
        neighbors.append([i - 1, j])
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    if j > 0:
        neighbors.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    return neighbors
        
```


```python

```


```python
# Trie implementation to store the words together with a terminating symbol
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
```


```python
def boggleBoard(board, words):
    """
    Explore the neighbor of each letter and return words that occur within the board.
    
    Space: WS + N*M, where W = words and S = length of longest word, and N * M dimensions of the visited auxiliary matrix
    Note that at most, we'll have S at the call stack, where S is the length of the longest word found in the board.
    Time: For every node, we go through all their neighbors... and for each neighbor, their neighbors as well....
    So at most, a node has eight neighbors. So that gives us 8X8X8X8X...X S-letters... simplified to (8^S)
    Worscase: (NM * 8^S + WS) Time complexity
    """
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    
    # Create an auxiliary matrix that keeps track of whether a letter position in the board is visited
    visited = [[False for letter in row] for row in board]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trie, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trie:
        return
    # mark as visited first
    visited[i][j] = True
    trie = trie[letter]
    if "*" in trie:
        # retrieve the stored word at the end symbol
        finalWords[trie["*"]] = True
    # get neighbors and explore each
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        # recursively explore each neighbor using DFS
        explore(neighbor[0], neighbor[1], board, trie, visited, finalWords)
    # after depth first searching neighbors is complete, unvisit the current letter
    visited[i][j] = False    
```


```python
words = ['this', 'is', 'a', 'simple', 'boggle', 'board', 'REPEATED', 'test', 'not', 'NOTRE-PEATED']
boggleBoard(board, words)
```




    ['this', 'is', 'simple', 'a', 'boggle', 'board', 'NOTRE-PEATED']




```python
boggleBoard(board, ['NOT', 'in', 'the', 'boardddd'])
```




    ['NOT']


