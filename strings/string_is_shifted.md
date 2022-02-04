## Problem
Given two strings A and B, return whether or not A can be shifted a number of times to get B.

For example, if `A = cdeab` and `B = abcde` return true. If `A = xyz and B = xzy` return false.  

### Solution
First, we should return false if the first and second string differ in length.

We can then concatenate one of the strings to itself, like (A + A) and check if B is in the concatenated string.
If the string is shifted, we will find it in the new string.


```python
def is_shifted(a, b):
    if len(a) != len(b):
        return False
    return b in a + a
```


```python
is_shifted("cdeab", "abcde")
```




    True




```python

```
