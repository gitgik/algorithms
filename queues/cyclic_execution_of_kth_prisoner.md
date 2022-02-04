## Problem

There are N prisoners standing at a circle, waiting to be executed. Executions start with the Kth person, and goes on clockwise, removing every successive Kth person until there's no one left.

Given N and K, determine where the prisoner should stand in order to be the last survivor.

For example, if N = 5, and k = 2, order of executions will be [2, 4, 1, 5, 3] so return 3.



```python
def last_executed(n, k):
    # create list of size n
    prisoners = [i for i in range(1, n + 1)]
    # use zero-based index
    i = k - 1
    
    # loop through cyclicly over prisoners list, until last visited prisoner
    while (n > 1):
        prisoners.pop(i)
        i = (i + k - 1) % len(prisoners)
        n -= 1
    return prisoners[0]
```


```python
last_executed(5, 2)
```




    3



Since popping from a random index in a list is O(N) and we are doing this N times, the solution runs in O(N^2).

We can improve the efficiency by using a double-ended queue. 

We will rotate our list in O(k) time by using a deque, so that we can pop elements at the end.
This allows us to eliminate each prisoner in O(k) time, thereby making the whole solution run in O(k * N)



```python
from collections import deque

def last_one_standing(n, k):
    prisoners = deque(range(1, n + 1))
    
    while (n > 1):
        prisoners.rotate(-k)
        prisoners.pop()
        
        n -= 1
        
    return prisoners[0]

```


```python
last_one_standing(5, 2)
```




    3


