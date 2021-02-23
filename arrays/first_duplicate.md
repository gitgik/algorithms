## Problem
Find the first duplicate value in an array of positive integers. Each integer value in the array is less or equal to the length of the array.

Sample input: [1, 2, 1, 3] (Notice the length of array is 3, so the largest value is 3)

Sample output: 1

Try finding a solution that runs in constant space.


```python
## solution (O(n) time | O(n) space)
def first_dup(array):
    unique = set()
    for i in array:
        if i in unique:
            return i
        unique.add(i)
    return -1
    
```


```python
first_dup([1, 2, 1, 3, 2])
```




    1



### Optimal Approach
We can take each element's value minus 1 and use it as an index. Where the index will fall in the array, we'll set that value to -ve. As we loop through the array,
if we end up at an element that is already set to -ve, we know we've found a duplicate.



```python
def first_duplicate(array):
    """Complexity: O(n) time | O(1) space"""
    
    i = 0
    while i < len(array):
        val = abs(array[i]) - 1
        # if we find a negative number, it's our first duplicate
        if array[val] < 0:
            return abs(array[val])
        else:
            # make the current value negative
            array[val] = -array[val]
        # increment i
        i += 1
    return -1
```


```python
first_duplicate([ 2, 1, 3, 4, 7, 6, 7])
```




    7


