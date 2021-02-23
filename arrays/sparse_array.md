## Problem

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

- `init(arr, size)`: initialize with the original large array and size.
- `set(i, val)`: updates index at i with val.
- `get(i)`: gets the value at index i.


```python
class SparseArray:
    def __init__(self, arr, size):
        self._dict = {}
        self.size = size
        
        for i, value in enumerate(arr):
            if value != 0:
                self._dict[i] = value
    
    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError("Out of bounds")
        if val != 0:
            self._dict[i] = val
            return
        elif val in self._dict:
            del self._dict[i]
        
    
    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Out of bounds")
        return self._dict.get(i, 0)
        
    
```


```python
arr = [0 for i in range(100)]
arr = [i for i in range(15)] + arr
sparse_array = SparseArray(arr, 20)
```


```python
sparse_array.get(14)
```




    14




```python
sparse_array.set(14, 12310)
```


```python
sparse_array._dict
```




    {1: 1,
     2: 2,
     3: 3,
     4: 4,
     5: 5,
     6: 6,
     7: 7,
     8: 8,
     9: 9,
     10: 10,
     11: 11,
     12: 12,
     13: 13,
     14: 12310}




```python
 
```
