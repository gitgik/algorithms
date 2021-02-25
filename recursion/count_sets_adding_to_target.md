## Problem
Given an array of non-negative integers, find the number of all the sets that add up to a given target.

Sample input:
```
[1, 2, 4, 5, 7],  Target = 7
```

The output is `3`, i.e {1, 2, 4}, {2, 5} and {7} all add up to 7


```python
def count_sets(arr, total):
    return helper(arr, total, len(arr) - 1, {})

def helper(arr, total, i, mem) -> int:
    key = f"{total}:{i}"
    if key in mem:
        return mem[key]
    
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0 
    elif total < arr[i]:
        to_return = helper(arr, total, i - 1, mem)
    else:
        to_return = helper(arr, total - arr[i], i - 1, mem) + helper(arr, total, i - 1, mem)
    mem[key] = to_return
    return to_return
```


```python
count_sets([1, 2, 4, 5, 7], 7)
```




    3


