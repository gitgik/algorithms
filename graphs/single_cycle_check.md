### Problem
You are given an array of integers. Each integer represents a jump of its value in the array. 

For instance, integer 2 represents two forward jumps in the array, while -3 represents 3 jumps backwards in the array. 

If the jump spills past the array bounds, it wraps over to the other side. 
For example, a jump of -1 from the first index brings back to the last index of the array. 

Write a function that returns a boolean if the jumps in the array form a single cycle. A single cycle occurs if starting from any index, the jumps visit each element exactly once until before landing back on the starting index.


```python
# solution: O(n) time | O(1) space
def has_single_cycle(array):
    elements_visited = 0
    current_index = 0
    while elements_visited < len(array):
        if elements_visited > 0 and current_index == 0:
            return False
        elements_visited += 1
        current_index = get_next_index(current_index, array)
    return current_index == 0


def get_next_index(current_idx, array):
    jump = array[current_idx]
    next_index = (current_idx + jump) % len(array)
    
    if next_index >= 0:
        return next_index
    else:
        # change negative index to be an actual positive index on the array
        return next_index + len(array)
```


```python
has_single_cycle([2, -1, 1, -2])
```




    True



The time complexity is O(n) since we have a single while loop that iterates through the entire array of length n,
while the space complexity is O(1) constant time, since we are not storing any auxilliary array, just a couple of variables. 


```python

```
