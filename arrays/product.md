## Problem
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Sample input:

```
[1, 2, 3, 4, 5]
```

Expected output:

```
[120, 60, 40, 30, 24].
```


```python
def product(array):
    """O(n) time | O(1) space"""
    prod = 1
    for i in array:
        prod *= i
    for i in range(len(array)):
        array[i] = prod // array[i]
    return array   
```


```python
product([3, 2, 1])
```




    [2, 3, 6]




```python
"""
For a solution that doesn't use division:

To solve this problem,
we need to take the product of each element before ith element, including i (prefix products) 
and then multiply with product of elements after i, including i (suffix products).

O(n) time and O(n) space because of two auxiliary arrays created.
"""
def productArray(A):
    prefixProducts = []
    for num in A:
        if not prefixProducts:
            prefixProducts.append(num)
        else:
            prefixProducts.append(prefixProducts[-1] * num)
    
    suffixProducts = []
    for num in reversed(A):
        if not suffixProducts:
            suffixProducts.append(num)
        else:
            suffixProducts.append(suffixProducts[-1] * num)
    suffixProducts = list(reversed(suffixProducts))
    
    for i in range(len(A)):
        if i == 0:
            A[i] = suffixProducts[i + 1]
        elif i == len(A) - 1:
            A[i] = prefixProducts[i - 1]
        else:
            A[i] = prefixProducts[i - 1] * suffixProducts[i + 1]
    return A
```


```python
productArray([3, 2, 1])
```




    [2, 3, 6]




```python
res = []
a = [1, 2, 3]
for i in reversed(range(len(a))):
    res.append(a[i])
    
```


```python
res

```




    [3, 2, 1]


