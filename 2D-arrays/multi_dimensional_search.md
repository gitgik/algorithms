### Multi-dimensional search
Given a multi-dimensional array consisting of either integers, floats, strings or other nested arrays, return an array containing only numerical values that occur inside the original array (integers, floats).


```python
from typing import List

def find_numbers(A , results) -> List:
    """Complexity analysis
        O(N ^ m) time | O(n) space, where N is the total number of elements in the outer array A, and m is the number of the highest dimensions in the array.
    """
    results = [] if results is None else results
    for index, value in enumerate(A):
        if type(value) is list:
            find_numbers(A[index], results)
        elif type(value) in (int, float):
            results.append(value) 
    return results
```


```python
A = [[[[1]], [2, 3],[], [[0, [3, 4], [7, 8, 9]]], [2.3, 9.8]]]
find_numbers(A, results=[])
```




    [1, 2, 3, 0, 3, 4, 7, 8, 9, 2.3, 9.8]




```python

```
