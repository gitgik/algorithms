### Problem: Number of ways to make change
Given a list of integers representing denominations and an integer representing a target amount of money, create a function that returns the number of ways to make change for that target value using the denominations.
Note that an unlimited amount of coins is at your disposal.


```python
## solution
def make_change(n, denoms):
    """
    Complexity:
        O(nd) time, where n = target amount, and d is the number of denominations
        O(n) space
    """
    # set a list of zeros, before we begin filling up their respective number of ways to make change
    ways = [0 for i in range(n + 1)]
    
    # base case: if we have zero target amount to make its change, only one way exists: not doing anything --> so it becomes 1, 
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            # check to see if the denom is less than amount, because we can't use a large denomination to make change for a smaller amount
            if denom <= amount:
                # add the current number of ways there are to the number of ways to generate that amount minus the denomnication
                ways[amount] += ways[amount - denom]
    return ways[n]
```


```python
make_change(5, [1, 5])

```




    2


