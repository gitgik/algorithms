```python
def fibonacci(n, memoize={1:0, 2: 1}):
    """
    Nth fibonacci number using memoization.
    
    O(n) space and time
    """
    if n < 0:
        raise TypeError('Value of n must be a positive integer')
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fibonacci(n - 1, memoize) + fibonacci(n - 2, memoize)
        return memoize[n]


def efficient_fibonacci(n):
    """
    nth fibonacci number iteratively.

    Complexity:
        O(n) time,
        O(1) space, since we are only storing two array values at any given time.
    """
    last_two = [0, 1]

    counter = 3
    while counter <= n:
        next_fibonacci = sum(last_two)
        last_two = [last_two[1], next_fibonacci]
        counter += 1
    # the else clause caters for the edge case of the first fibo number == 0
    return last_two[1] if n > 1 else last_two[0]
```


```python
efficient_fibonacci(12)
```




    89




```python

```
