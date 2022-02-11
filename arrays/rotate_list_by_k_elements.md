## Problem

Write a function that rotates a list by k elements.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 

Try solving this without creating a copy of the list.

## Solution
We can rotate a list without creating a copy by moving each element down by one, k times. We must wrap around the list as well.


```python
def rotate(array, k):
    n = len(array) - 1
    for _ in range(k):
        first_element = array[0]
        for i in range(n):
            array[i] = array[i + 1]
        array[n] = first_element
    return array
```


```python
rotate([1,2,3,4,5], 2)
```




    [3, 4, 5, 1, 2]



Although this takes constant space, this will take O(n * k) time.

We can use a different approach.
First, we transform the array into two subarrays:
- array[k:], 
- array[:k]

By reversing these two subarrays and then reversing the whole subarray we can effectively rotate the array in linear time, and constant space.


```python
def rotate(array, k):
    reverse(array, 0, k - 1)
    reverse(array, k, len(array) - 1)
    reverse(array, 0, len(array) - 1)
    return array

def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
```


```python
rotate([1, 2, 3, 4, 5, 6, 7], 3)
```




    [4, 5, 6, 7, 1, 2, 3]


