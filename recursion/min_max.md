### Problem
Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.


```python
def min_max(array):
    if len(array) == 1:
        return array[0], array[0]
    elif len(array) == 2:
        return (array[0], array[1]) if array[0] < array[1] else (array[1], array[0])
    else:
        mid = len(array) // 2
        left_min, left_max = min_max(array[:mid])
        right_min, right_max = min_max(array[mid:])
        return min(left_min, right_min), max(left_max, right_max)

```


```python
min_max([1, 2, 3, 4])
```




    (1, 4)



For array of size N, we are breaking down the problem into two subproblems of size `N / 2` plus `2` comparisons. 

```python
# Recursively break down array
[4, 2, 7, 5, -1, 3, 6] 
[[4, 2, 7, 5], [-1, 3, 6]]
[[[4, 2], [7, 5]], [[-1, 3], [6]]]

# Base case: reorder so that smaller comes before larger
[[[2, 4], [5, 7]], [[-1, 3], [6, 6]]]

# Merge to find min and max
[[min(2, 5), max(4, 7)], [min(-1, 6), max(3, 6)]]
[min(2, -1), max(7, 6)]
[-1, 7] 
```


```python

```
