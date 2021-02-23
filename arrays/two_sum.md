```python
"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def twoSum(array, k):
    """Return true if numbers in the array add to k, else false | O(n) time and space"""
    seen = set()
    for i in array:
        if k - i in seen:
            return True
        seen.add(i)
    return False
```


```python
twoSum([1, 1, -1, 1, 6, 9, 3, 1], 10)
```




    True




```python
# [3, 2, 6, 1, 0], k = 4  ==> [0, 1, 2, 3, 6]

def twoSum(A, k):
    """Sort the list first O(n log n) for constant space O(1)"""
    A.sort()
    left = 0
    right = len(A) - 1
    
    while left < right:
        totalSum = A[left] + A[right]
        if totalSum > k:
            right -= 1
        elif totalSum < k:
            left += 1
        else:
            return True
    return False

```


```python
twoSum([3, 2, 6, 1, -1], 0)
```




    True




```python

```
