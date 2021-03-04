## Problem

Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in `O(log N)` time.

## Solution
We can't use binary search to locate the element because involves dividing by two to get the middle element. 

We can use Fibonacci search to get around this limitation. The idea is that fibonacci numbers are used to locate indices to check in the array, and by cleverly updating these indices, we can efficiently locate our element.

Let `p` and `q` be consequtive Fibonacci numbers. `q` is the smallest Fibonacci number that is **greater than or equal to** the size of the array. We compare `x` with `array[p]` and perform the following logic:

1. If `x == array[p]`, we have found the element. Return true.
2. If `x < array[p]` move p and q down two indices each, cutting down the largest two elements from the search.
3. If `x > array[p]` move p and q down index each, and add an offset of p to the next search value.

If we have exhausted our list of Fibonacci numbers, we can be assured that the element is not in our array.


Let's go through an example.

First, we need a helper function to generate the Fibonacci numbers, given the length of the array => N.


```python
def get_fib_sequence(n):
    a, b = 0, 1
    
    sequence = [a]
    while a < n:
        a, b = b, a + b
        sequence.append(a)
    return sequence
```

Suppose we have array 
```
[2, 4, 10, 16, 25, 45, 55, 65, 80, 100]
```

Since there are 10 elements in the array, the generated sequence of Fibonacci numbers will be 
```
[0, 1, 1, 2, 3, 5, 8, 13]
```

So the values of p and q are: `p == 6, q == 7` (The second last and last indices in the sequence)   

Now suppose we are searching for `45`, we'll carry out the following steps:

- Compare 45 with `array[fib[p]] => array[8]`. Since 45 < 80, we move p and q down two indices. p = 4, q = 5.
- Next, compare 45 with `array[fib[p]] => array[3]`. Since 45 > 16, we set p = 3 and create an offset of 2. So p = 5, q = 4. 
- Finally, we compare 45 with `array[fib[p]]`. Since array[5] == 45, we have found x.



```python
def fibo_search(array, x):
    n = len(array)
    fibs = get_fib_sequence(n)
    
    p, q = len(fibs) - 2, len(fibs) - 1
    offset = 0
    
    while q > 0:
        index = min(offset + fibs[p], n - 1)
        if x == array[index]:
            return True
        elif x < array[index]:
            p -= 2
            q -= 2
        else:
            p -= 1
            q -= 1
            offset = index
    return False
```


```python
fibo_search([2, 4, 10, 16, 25, 45, 55, 65, 80, 100], 45)
```




    True




```python

```
