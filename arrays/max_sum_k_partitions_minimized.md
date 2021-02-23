## Minimized max sum of k partitions

Given an array of numbers and an integer K, split the array into K partitions such that the maximum sum of any partition is minimized. Return the sum.

Sample input:

```
array = [5, 1, 2, 7, 3, 4]  k = 3
```

Output:

```
Return 8

since the optimal partition is 
[5, 1, 2], [7], [3, 4]
```


### Approach
- We know that the sum can't be smaller than the largest element in the list
- It also can't be largest than the sum of the whole list

We can check each value between the max element and the array sum until we find the smallest one that works. To make the search better, we can perform a binary search.


```python
def max_partition_sum(array, k):
    left, right = max(array), sum(array)
    
    while left < right:
        mid = (left + right) // 2
        if can_partition(array, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

def can_partition(array, limit, k):
    total = 0
    partitions = 1
    
    for num in array:
        if total + num > limit:
            
            total = num
            partitions += 1
            if partitions > k:
                return False
        else:
            total += num
    return True
```


```python
max_partition_sum(
    array=[5, 1, 2, 7, 3, 4],
    k=3
)
```




    8



In the `can_partition`, we must check for a given candidate limit, whether an array can be split into k partitions such that no partition exceed this candidate limit. 

Here, we can use a greedy solution:
- We traverse the list, adding elements into the current partition up until its sum exceeds the limit. 
- In this case, we start a new partition with the current element.
- If the number of partitions required is more than k, we know it is impossible, so we increment the left lower bound side by 1 (so as to eventually reduce the partitions to come close to or equal k).

Each call to can_partition runs in `O(N)` time, since we must traverse the entire array in the worst case. 
The number of calls is at most log R, where R = (array sum - max element of array).

So overall, the time complexity is O(N log R)


```python

```
