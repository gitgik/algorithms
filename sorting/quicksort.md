### Quicksort
Here's a simpler implementation to follow:



```python
def qsort(A):
    """Complexity:
         Average Case: O(n log n) time | O(log n) space,
         Worst Case: (When the array is sorted) --> O(n^2) time | O(n) space (Note: Height of the call stack is n)
    """
    
    if len(A) < 2:
        # array is already sorted
        return A
    
    # get the pivot from the middle of the array
    pivot = A[(len(A) - 1) // 2]
    left_subarray = [i for i in A[1:] if i <= pivot]
    right_subarray = [i for i in A[1:] if i > pivot]
    
    return qsort(left_subarray) + [pivot] + qsort(right_subarray)
```


```python
array = [5, 4, 2, 10, 0, -12, 6]
qsort(array)
```




    [-12, 0, 0, 6, 10, 10, 10]




```python
## Quicksort
## O(n log(n)) time | O(log (n)) space
def quicksort(array):
    quicksort_helper(array, 0, len(array) - 1)
    return array

def quicksort_helper(array, start_idx, end_idx):
    # base case
    if start_idx >= end_idx:
        return
    
    
    pivot_idx = start_idx
    left_idx = pivot_idx + 1
    right_idx = end_idx
    

    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    
    # we've gotten to a point where the left pinter is greater than the right, so swap pivot with right pointer
    swap(pivot_idx, right_idx, array)
    
    # now, call the quick sort algorithm to the resulting left and right subarrays.
    left_subarray_is_smaller = (right_idx - 1) - start_idx < end_idx - (right_idx + 1)
    if left_subarray_is_smaller:
        # left subarray is smaller so start with it first
        quicksort_helper(array, start_idx, right_idx - 1)
        quicksort_helper(array, right_idx + 1, end_idx)
    else:
        # work on right subarray first
        quicksort_helper(array, right_idx + 1, end_idx)
        quicksort_helper(array, start_idx, right_idx - 1)
    

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
```


```python
array = [3, 1, 2]
quicksort(array)
```




    [1, 2, 3]




```python
## Feel free to run these tests
import unittest

class QuickSortTestCase(unittest.TestCase):
    def test_case_1(self):
        array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
        expected = [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10]
        self.assertEqual(quicksort(array), expected)
        
    def test_case_2(self):
        array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
        expected = [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
        self.assertEqual(quicksort(array), expected)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
```
