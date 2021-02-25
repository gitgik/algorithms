```python
def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]
```


```python
def fibo(n, memoize={1:0,2:1}):
    if n < 2:
        return n
    
    memoize[n] = fibo(n - 1, memoize) + fibo(n - 2, memoize)
    return memoize[n]
```


```python
fibo(5)
```




    5




```python
fibonacci(6)
```




    8




```python

```
