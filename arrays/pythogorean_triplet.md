## Pythogorean triplet

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.


```python
def triplet(array):
    array = [i ** 2 for i in array]
    for a in array:
        for b in array:
            for c in array:
                if a + b == c or a + c == b or b + c == a:
                    return True
    return False
```


```python
triplet([10, 8, 6, 4, 3, 0])
```




    True



This runs at O(N**3) cubic time, where N is the number of elements in the array. We can make it a little more faster to run at a quadratic time.

# Better solution
We first sort the squared array. This allows us to work with the assumption that `a < b < c`, and that a, b and c exist this way in the newly sorted squared array.

Assume that `a=1st element, b=2nd, c=3rd`. We can use the following algorithm to find if there are triplets:

- If a + b < c, increment a so that new a = the second element in list.
- If a + b > c, decrement b so that new b = the third-last element in list.
- If a + b == c, return True.
- If a and b cross paths, we know there cannot be any more solutions with our current value of c, so we increment c and try again.


```python
def triplet(array):
    """O(N**2) time"""
    array = sorted([_ ** 2 for _ in array])
    
    for c in range(2, len(array)):
        a = 0
        b = c - 1
        while a < b:
            if array[a] + array[b] == array[c]:
                return True
            elif array[a] + array[b] < array[c]:
                a += 1
            else:
                b -= 1
    return False
```


```python
triplet([11, 4, 78, 23, 7, 2, 4, 3, 5])
```




    True




```python

```
