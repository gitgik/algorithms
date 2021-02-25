## Problem
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14

## Solution
Because the greatest common divisor is associative, gcd of multiple numbers: say `a, b, c` is equivalent to 
```
gcd(gcd(ab),c)
```
By definition, if the divisor divides gcd(a, b) and c, it must divide a and b as well.

The GCD of multiple numbers `a, b, ... n` can be obtained by **iteratively computing the GCD of `a and b`, and GCD of the result of that with `c` and so on.**


```python
def gcd(numbers):
    n = numbers[0]
    for num in numbers[1:]:
        n = _gcd(n, num)
    return n
```

A naive implementation might try every integer from 1 to min(a, b) and see of it divides the larger:


```python
def _gcd_naive(a, b):
    # find smallest value, largest value of the two
    smaller, larger = min(a, b), max(a,b)
    # iteratively check every integer from the smallest value to 1.
    for divisor in range(smaller, 0, -1):
        if larger % divisor == 0:
            return divisor
```

A more efficient method is the Euclidean algorithm which follows a recursive formula:

```
gcd(a, 0) = a
gcd(a, b) = gcd(b, a % b)
```


```python
def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)
```


```python
# time to test it out
gcd([42, 56, 14, 7])
```




    7



Here's a more memory-efficient method that works bottom up:


```python
def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# test it out
gcd([0, 64, 256, 128])
```




    64



For more details check out this video tutorial on how [Euclidean algorithm](https://www.youtube.com/watch?v=p5gn2hj51hs) works.


