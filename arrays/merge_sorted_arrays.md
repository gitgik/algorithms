## Problem
Given a non-empty list of non-empty sorted arrays, write a function to merge the lists into one sorted list.

Sample input:
```python
arrays = [
    [1, 5, 9, 21], 
    [-1, 0], 
    [-124, 81, 121], 
    [3, 6, 12, 20, 150]
]
```
The function should return:

```python
[-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
```

### Solution
The first element in each array is the smallest element on their respective arrays. 

We can perform the following steps:

- To find the smallest element to add to the final sorted list, we pick the first elements from each array and obtain the smallest of them.
- Once we find the smallest integer, we move to the next index on the array the integer belongs to.
- We repeat this process until we reach the last index on each array. We break out of the loop and return the sorted list.

This will run in O(nk) time and O(n + k) space, where n = number of array elements and k = number of arrays.


```python
def merge(arrays):
    sorted_list = []
    element_indices = [0 for array in arrays]
    while True:
        smallest_items = []
        for i in range(len(arrays)):
            array = arrays[i]
            element_idx = element_indices[i]
            if element_idx == len(array):
                continue
            smallest_items.append({
                'array_index': i,
                'num': array[element_idx]
            })
        if len(smallest_items) == 0:
            break

        next_item = get_min_value(smallest_items)
        sorted_list.append(next_item['num'])
        element_indices[next_item['array_index']] += 1
    return sorted_list


def get_min_value(items):
    min_value_index = 0
    for i in range(1, len(items)):
        if items[i]["num"] < items[min_value_index]["num"]:
            min_value_index = i
    return items[min_value_index]
```


```python
arrays = [
    [1, 5, 9, 21], 
    [-1, 0], 
    [-124, 81, 121], 
    [3, 6, 12, 20, 150]
]
merge(arrays)
```




    [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]




```python

```
