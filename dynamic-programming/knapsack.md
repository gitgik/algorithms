## Knapsack Problem
You are given an array of arrays. Each subarray in this array contains two integer elements: the first represents an item value, the second an item's weight.

You are also given an integer representing the maximum capacity of the knapsack that you have.

Your goal is to fit items that will collectively fit within the knapsack's capacity while maximizing on their combined value.

Write a function that returns the maximum combined value of the items you'd pick, as well as an array of the item indices picked.

Sample Input: [[1,2],[4,3],[5,6],[6,7]], 10
Sample Output: 10, [1, 3]




```python
def knapsack(items, capacity):
    """O(nc) time | O(nc) space, where n == number of items, c == capacity"""
    knapsack_values = [[0 for col in range(capacity + 1)] for row in range(len(items) + 1)]
    
    for row in range(1, len(items) + 1):
        value = items[row - 1][0]
        weight = items[row - 1][1]
        for col in range(capacity + 1):
            if weight > col:  # col here represents a given capacity
                knapsack_values[row][col] = knapsack_values[row - 1][col]
            else:
                knapsack_values[row][col] = max(
                    knapsack_values[row - 1][col],
                    knapsack_values[row - 1][col - weight] + value
                )
    
    return [knapsack_values[-1][-1], backtrack_items(knapsack_values, items)]

def backtrack_items(values, items):
    """
    Backtracks from the bottom right of the 2d array, finding all the items that were put in the knapsack.
    """
    results = []
    row = len(values) - 1
    col = len(values[0]) - 1
    
    while row > 0:
        if values[row][col] == values[row - 1][col]:
            row -= 1
        else:
            results.append(row - 1)
            col -= items[row - 1][1]
            row -= 1
    return list(reversed(results))
```


```python
# test it out
capacity = 10
items = [[1, 3], [4, 3], [5, 6], [6, 7]]

knapsack(items, capacity)
```




    [10, [1, 3]]



### Unit Tests


```python
# unit tests
import unittest

class KnapsackTestCase(unittest.TestCase):
    def test_case_1(self):
        capacity = 10
        items = [[1, 3], [4, 3], [5, 6], [6, 7]]
        expected = [10, [1, 3]]
        self.assertEqual(knapsack(items, capacity), expected)
        
    def test_case_when_capacity_is_zero(self):
        capacity = 0
        items = [[1, 3], [4, 3], [5, 6], [6, 7]]
        expected = [0, []]
        self.assertEqual(knapsack(items, capacity), expected)
        
        
if __name__ == "__main__":
    unittest.main(argv=[""], exit=False)
```
