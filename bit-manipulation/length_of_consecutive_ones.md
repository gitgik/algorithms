## Problem

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

### 1st Approach
The simplest way to solve this is to keep track of a counter of the maximum number of consecutive 1's seen. Once we get a longer run of set bits, we update the counter.


```python
def find_length(n):
    max_length = current_length = 0
    bits = bin(n)[2:]
    
    for bit in bits:
        if bit == "1":
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length        
```


```python
find_length(156)
```




    3



### 2nd approach
The solution above runs in O(N) time. 
A faster way to solve this is to manipulate bits directly.

If we perform the operation `X & (X << 1)`, the consecutive runs of 1 must decrease by 1. By shifting the current number first, all but one of the set bits in the original number will correspond with the set bits in the shifted number.

For instance:

```
  10011100
& 00111000
-----------
  00011000
```

With this in mind, we can continue to AND our input with a shifted version of itself until we reach 0. The number of times we perform this operation will be our answer.


```python
# 156 & (156 << 1)
bin(0b10011100 & (0b10011100 << 1))
```




    '0b11000'




```python
def max_length_consecutive_ones(n) -> int:
    max_length = 0
    while n:
        max_length += 1
        n = n & (n << 1)
    return max_length
```


```python
max_length_consecutive_ones(0b10011100)  # You can use an integer as well
```




    3



While the worst case here is the same as the first approach, the number of operations we perform is just the length of the longest consecutive run of 1s.


```python

```
