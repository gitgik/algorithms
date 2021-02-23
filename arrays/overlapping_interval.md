### Problem

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

## Solution
We can do this by sorting all the intervals by their start time. 

When looking at the current interval, if it overlaps with the previous one we can just remove it. If the previous 


```python
def merge_overlaps(array):
    if len(array) == 1:
        return array
    array.sort(key=lambda x: x[0])  # O(N log N) sorting
    i = 1
    while i < len(array):
        if is_subset(array[i], array[i - 1]):
            # current is subset of previous, remove current
            del(array[i])
        elif is_subset(array[i - 1], array[i]):
            # previous is subset of current, remove previous
            del(array[i - 1])
        else:
            i += 1
    return array

def is_subset(subset, parent) -> bool:
    return True if parent[0] <= subset[0] and subset[1] <= parent[1] else False

```


```python
array = [(1, 3), (5, 8), (4, 10), (20, 25)]
merge_overlaps(array)
```




    [(1, 3), (4, 10), (20, 25)]




```python
arr = [(1, 10), (2, 3), (11, 12), (3, 4), (7, 8), (9, 10)]
merge_overlaps(arr)
```




    [(1, 10), (11, 12)]



Since we have to sort the intervals, this runs in **O(N log N)** time. We are deleting the overlapping intervals in-place so the solution will run in **O(1)** space.


```python

```
