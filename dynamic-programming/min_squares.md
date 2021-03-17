## Minumum squares that sum to n

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

### Naive Approach
We can use a recursive approach to naively solve this problem:
- Iterate through from 1 to sqrt(n)
- Recursively find the minimum number of squares needed to sum to `n - i * i`
- Pick the minimum of those plus 1
- Base case is when n == 0


```python
from math import inf

def num_squares(n):
    if n == 0:
        return 0
    
    min_num_squares = inf
    i = 1
    while n - i * i >= 0:
        min_num_squares = min(min_num_squares, num_squares(n - i * i) + 1)
        i += 1
        
    return min_num_squares
```


```python
num_squares(27)
```




    3



### DP Approach
Since this takes exponential time, we can speed it up by using a cache with dynamic programming.
- Create an array to represent the cache, with the first index containing zero. The rest contain infinity value.
- Starting from index 1, fill up the minimum number of squares for each index using the previously computed min values.
- Return `cache[n]`


```python
from math import inf

def min_num_squares(n):
    cache = [inf for i in range(n + 1)]
    cache[0] = 0
    
    for i in range(n + 1):
        j = 1
        while j * j <= i:
            cache[i] = min(cache[i], cache[i - j * j] + 1)
            j += 1
    return cache[n]
```


```python
min_num_squares(13)
```




    2



This will run on O(n^2) time and O(n) space


```python

```
