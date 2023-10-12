Given a list of integers, return the largest product of three of the integers. You can assume that the list contains at least 3 integers. 

For example, if the list is [-5, -10, -10, 5, 2, 3], we should return 500, since that's -10 * -10 * 5.

## First approach
We will need to account for negative numbers in the array. 

If the largest product that can be made includes a negative number, we need to have two so as to cancel out the negatives. 

So, we can take the larger of:

- The three largest numbers
- The two smallest (most negative) numbers, and the largest number


```python
def product(array) -> int:
    # first find if there are two large -ves, multiply them with the largest positive.
    # sort, multiply last 3
    # return max(first, second)
    array.sort()
    first_product = array[0] * array[1] * array[-1]
    second_product = array[-1] * array[-2] * array[-3]
    return max(first_product, second_product)
```


```python
array = [-5, -10, -10, 5, 2, 3]
product(array)
```




    500



This runs in O(N log N) time since we have to sort the input array.

## second approach without sorting.
We can find an O(N) solution by manually looking for the largest elements in the array.



```python
def product(A) -> int:
    max1, max2, max3, min1, min2 = float("-inf"), float("-inf"), float("-inf"), float("inf"), float("inf")
    
    for i in A:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = x
            
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    
    return max(max1 * max2 * max3, min1 * min2 * max1)
            
```


```python
product(array)
```




    500




```python

```
