## Search in log (N) using pivot

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

### O(N) Approach

A sraightforward way to solve this is to use two pointers, left and right, to search inwards. On the left side, we should expect an ascending order. If a value breaks this pattern, we have hit the pivot, so we return the value after the pivot. 
Similarly, on the right side, we should expect a descending order. If we get a value that breaks the order, we know we've hit the pivot. So we return the value at pivot + 1.


```python
def smallest(array: list) -> int:
    left = 0
    right = len(array) - 1
    
    while left < right:
        if array[left] > array[left + 1]:
            return array[left + 1]
        if array[right] < array[right - 1]:
            return array[right]
        left += 1
        right -= 1
```


```python
smallest([16, 17, 9, 10, 11])

```




    9




```python
smallest([2, 1])
```




    1



### O(log N) Approach
We'll use binary search to solve it. 

Let's look at what happens if we split our list at some point. If the value at our splitting point is less than the last element in the list, we know the right half is sorted, so the minimum element must lie in the left half (including the midpoint). Otherwise, it must lie in the right half.

We can apply this routine repeatedly to cut in half the area where the minimum element must be. Eventually we will reach a point where the lowest and highest indices we are looking at are the same, so we return the element at this index.


```python
def find_min_element(arr:list) -> int:
    low = 0
    high = len(arr) - 1
    return helper(arr, low, high)

def helper(array, low, high):
    if low == high:
        return array[low]
    
    mid = (high + low) // 2
    if array[mid] < array[high]:
        high = mid
    else:
        low = mid + 1
    return helper(array, low, high)
```


```python
find_min_element([4, 5, 6, 0, 1, 2])
```




    0




```python

```
