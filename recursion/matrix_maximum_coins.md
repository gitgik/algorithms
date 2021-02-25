### Problem 
You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

```python
0 3 1 1
2 0 0 4
1 5 3 1
```

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

### Approach
Consider the following matrix,

```
0 2 3
5 4 9
6 7 1
```

- If we are at 1, the most coins we can collect is ` 1 `
- If we start at 7, the most coins we'll co is `7 + 1`
- If we start at 9, the most coins we can have is `9 + 1`
- If we start at 4, the most coins we can collect is `max(7 + 1,  9 + 1)`

This is a recursive problem. 

The base case will be when we get to the bottom-right corner of the matrix – the most amount of coins we can collect at that point is that cell.
This leads to the following solution:


```python
def collect_coins(matrix, r=0, c=0, cache=None):
    if cache is None:
        cache = {}
    
    is_bottom = (r == len(matrix) - 1)
    is_rightmost = (c == len(matrix[0]) - 1)
    
    if (r, c) not in cache:
        if is_bottom and is_rightmost:
            cache[r, c] = matrix[r][c]
        elif is_bottom:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r, c + 1, cache)
        elif is_rightmost:
            cache[r, c] = matrix[r][c] + collect_coins(matrix, r + 1, c, cache)
        else:
            cache[r, c] = matrix[r][c] + max(collect_coins(matrix, r, c + 1, cache), collect_coins(matrix, r + 1, c, cache))
    return cache[r, c]
```


```python
matrix = [
  [0, 3, 1, 1],
  [2, 0, 0, 4],
  [1, 5, 3, 1]
]
collect_coins(matrix)
```




    12


