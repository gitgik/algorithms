### Problem
You are given an array of length N, where each element i represents the number of ways we can produce i units of change. For example, [1, 0, 1, 1, 2] shows that there is only one way to make [0, 2, or 3] units, and 2 ways of making 4 units.

Given such an array, determine the denominations that must be in use. In the case above, there must be coins with value 2, 3, and 4.

### Approach

There are two situation that will make the value at that index i be incremented:
1. Coin `i` is one of the denominations
2. Another coin `j` is one of the denominations and the value of array[i - j] is also non-zero
    
For each index:
- Check the lower denominations j that are known to be part of the solution.
- Each time we find `i - j` to be non-zero, we have encountered one of the ways of getting to element `i`, so we decrement the value at that index by 1.
- If after going through all coins and the value at that index is still positive, we know that we must include `i` as part of the solution

We must take note not to double count. For example, when `i == 7` and [3, 4] are in our solution set, that is one way of producing 7.
When two coins sum up to an index, only the lower one cause us to decrement the value at that index.

    


```python
def find_denominations(array):
    coins = set()
    # start from index 1, and start counting from 1 (not zero-based index)
    for i, val in enumerate(array[1:], 1):
        if val > 0:
            for j in coins:
                if array[i - j] > 0 and (i - j not in coins or i - j <= j):
                    val -= 1
            if val > 0:
                coins.add(i)
    return coins
```


```python
find_denominations([1, 0, 1, 1, 2])
```




    {2, 3, 4}



The time complexity of this algorithm is O(M * N), where M is the number of coins in our solution and N is the length of our input. 

The space complexity will be O(M), since we require extra space to store the set of solution coins.


```python

```
