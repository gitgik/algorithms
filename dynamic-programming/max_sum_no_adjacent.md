### Max sum no adjacent
Given a array of integers, find the maximum sum of non-adjacent elements in the array, returning the sum. If the sum can't be generated, return 0.

```
Sample input: [1, 2, 4, 20]
Sample output: 22
```


```python
def maxSubsetNoAdjacent(array):
    """Clone the input array and call it maxSum.
    Then find the max sum generated from index 0 to the current index, storing them at those indices. Formula: maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + current_index_value)).
    Finally, return the last index. (this will have the maximum sum stored)
    
    O(n) time | O(n) space, where n == length of input array
    """
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return A[0]
    
    max_sums = array[:]
    max_sums[1] = max(max_sums[0], max_sums[1])
    
    for i in range(2, len(array)):
        max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
    return max_sums[-1]
```


```python
A = [1, 2, 3, 4]
maxSubsetNoAdjacent(A)
```




    6



Instead of creating an entire array, we can reduce the problem to `O(1) space`  by keeping track of the last two values only.


```python
def max_subset_no_adjacent(A):
    """O(n) time | O(1) space."""
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return A[0]
    previous = A[0]
    max_sum = max(A[0], A[1])
    for i in range(2, len(A)):
        current = max(max_sum, previous + A[i])
        previous = max_sum
        max_sum = current
    return max_sum
```


```python
max_subset_no_adjacent(A)
```




    6




```python

```
