####  Problem
Given an array of positive integers denoting coin denominations and a single non-negative integer representing a target amount of money, 

implement a function to find the minimum number of coins needed to make change for the target using the given coin denominations.

If it's impossible to make change for the target amount, return -1.

Sample input: 7,  [1, 2, 5] denominations

Sample output: 2 (coins) i.e (1x2, 5x1)


```python
# solution
def min_change(target, denominations):
    """
    Complexity:
        Space: O(N), where N == size of array obtained from the target
        Time: 0(N * d), where d == number of denominations provided.
    """
    if target == 0:
        return 0
    
    coin_list = [float('inf') for i in range(target + 1)]
    # make the first index value to be zero
    coin_list[0] = 0
    
    # for each denomination given
    for denom in denominations:
        # iterate through the coin list, 
        # updating each value to be the minimum num of coins required to make change for the respective index
        for amount in range(len(coin_list)):
            if denom <= amount:
                coin_list[amount] = min(coin_list[amount], coin_list[amount - denom] + 1)
    
    return coin_list[target] if coin_list[target] != float('inf') else -1
            
```


```python
# run it
min_change(7, [1, 2, 5])
```




    2




```python

```
