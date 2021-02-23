## Maximum product of three
Given an list of integers, return the maximum product that can be formed by multiplying any three integers.

Sample input:
```
[-10, -20, 5, 2, -7, 3]
```

Output:
```
1000  (-10 * -20 * 5)
```

Assume that the list has at least 3 integers.

## Approach
If all the integers were positive, we'd simply take the three largest numbers of the array i.e sort and return the last three elements.

However, we need to account for negative numbers in the array. If the largest product can be made by negative numbers, we'd need to have two so as to cancel out the negatives. So, we can take the larger of:

- The three largest numbers
- The two smallest (most negative) numbers, and the largest number


```python
def product(array) -> int:
    """O(N log N) time, because of sorting."""
    
    array.sort()
    max1, max2, max3 = array[-1], array[-2], array[-3]
    min1, min2 = array[0], array[1]
    return max(max1 * max2 * max3, min1 * min2 * max1)
    
```


```python
product([-10, -20, 5, 2, -7, 3])
```




    1000



# 2nd Approach
We can look for the largest elements manually and create a solution that runs on O(N) time.


```python
from math import inf

def max_product(array) -> int:
    max1, max2, max3 = -inf, -inf, -inf
    min1, min2 = inf, inf
    
    for i in array:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = i
        
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
        
    return max(max1 * max2 * max3, max1 * min1 * min2)
```


```python
max_product([-10, -20, 5, 2, -7, 3])
```




    1000




```python

```
