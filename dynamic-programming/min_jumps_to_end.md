### Problem
Given an array of positive integers, find the minimum number of jumps required to get from the first index to the final one.

Sample input:
```
array = [4, 2, 1, 1, 3, 1, 2, 1]
```

Sample output:
```
2   (4 --> 3 --> 1)
```

Note that jumping from index `i` to index `i + X` is still one jump, regardless of the size of X

We build a new array to store minimum number of jumps from index 0 to rest of indices. 
    
The first is 0. (since step required to jump from an index to itself is zero)

Progressively build the array using the previously computed min jumps.


```python
def minJumps(array):
    """O(n) space | O(n^2) time, since for every index, we are checking all elements to its left"""
    
    jumps = [float('inf') for i in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            # check if value before i (array[j]), if the step j is added to it, will it exceed i
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    # the last element contains the min jumps required to reach the end of array
    return jumps[-1]        
```


```python
minJumps([4, 2, 1, 1, 3, 1, 2, 1])
```




    2


