## Find smallest missing positive integer
Given an array of integers, find the first missing **positive** integer in linear time and constant space. 

In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.

## Solution
We could sort the list first but that takes O(N log (N)). We want a solution that works in O(N) time.

We can follow the following steps to solve it:

- pop the smallest value in the list. 
- If it's less than 0, we pop the next min value. 
- If not, check whether the `smallest + 1` exists in the array. Continue looping if this value exists in the array. Otherwise, return `smallest + 1`.
- If we continously pop to the last element, return 1. This means that all the values were negative and the smallest positive integer is 1.


```python
def first_missing_positive(array) -> int:
    if len(array) == 0:
        return 1
    
    while len(array) > 0:
        smallest = array.pop(array.index(min(array)))
        if smallest < 0:
            continue
        elif smallest + 1 in array:
            continue
        else:
            return smallest + 1
    return 1
```


```python
first_missing_positive([-1, 0, 4, 5])
```




    1



Another way, although running in O(N) space, is to put all the numbers in a set and init a counter to 1. Then, continously increment the counter and check whether the value exists in the set.


```python
def first_missing_positive(nums) -> int:
    nums_set = set(nums)
    i = 1
    while i in nums_set:
        i += 1
    return i
```


```python
first_missing_positive([0, 1, 2, 3, 4])
```




    5


