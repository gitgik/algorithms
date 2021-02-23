## Problem
Given a list of non-negative integers representing an elevation map where the width of each map is one, compute the amount of water it is able to collect after raining.

![](../images/rainwatertrap.png)

The above elavation map is represented by the array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped. 6 units of water.

Sample input: [0,1,0,2,1,0,1,3,2,1,2,1]
Sample output: 6


```python
## solution
def trap(array):
    """Complexity: O(n) time | O(1) space"""
    trapped_water = 0
    left = 0
    right = len(array) - 1
    max_height = 0
    
    while left < right:
        if array[left] < array[right]:
            if array[left] > max_height:
                max_height = array[left]
            else:
                trapped_water += max_height - array[left]
            left += 1
        else:
            if array[right] > max_height:
                max_height = array[right]
            else:
                trapped_water += max_height - array[right]
            right -= 1
    return trapped_water
```


```python
array = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(array)
```




    6




```python
# unit tests
import unittest

class TrapTestCase(unittest.TestCase):
    def test_case_0(self):
        array = list(range(10))
        self.assertEqual(trap(array), 0)
        
    def test_case_1(self):
        array = [3, 1, 2, 0, 3, 0, 1, 2]
        self.assertEqual(trap(array), 9)
        
        

# if __name__ == "__main__":
#    unittest.main(argv=[""], exit=False)
```
