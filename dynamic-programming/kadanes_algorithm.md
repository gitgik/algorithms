### Problem
Given an array of integers, find the largest possible sum of contiguous subarray within the given array.


```python
## solution
def kadanes_algorithm(array):
    """Complexity: O(n) time | O(1) space"""
    
    local_max = global_max = array[0]
    for i in range(1, len(array)):
        # the local maximum for an index is always => max(array[i], local_max of array[i - 1])
        local_max = max(array[i], array[i] + local_max)
        global_max = max(global_max, local_max)
    return global_max
```


```python
array = [-3, 4, -1, 2, 1, -5, 4, -12, 3, -7]
kadanes_algorithm(array)
```




    6




```python
## unit tests to validate solution
import unittest

class KadenesTestCase(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_sum = 55
        self.assertEqual(kadanes_algorithm(array), expected_sum)
        
    def test_case_2(self):
        array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_sum = 6
        self.assertEqual(kadanes_algorithm(array), expected_sum)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```


```python
kadanes_algorithm([1, -1, 2, 3, -6])
```




    5




```python

```
