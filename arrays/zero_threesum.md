### Zero threesum
Given an array of integers return three numbers that sum up to zero. The function should also get rid of duplicate triplets.

Sample input
```python
nums = [-1, -1, 0, 1, 2]
```

Sample output
```python
[[-1, -1, 2], [-1, 0, 1]]

```


```python
def threesum(nums):
    """O(n^2) time ---> since (N^2 from two loops + Nlog(N) from sorting) is asympotically equivalent to O(N^2))  |  O(nlog n) space"""
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            triplet_sum = nums[left] + nums[i] + nums[right]
            if  triplet_sum == 0:
                triplets.append(sorted([nums[left], nums[i], nums[right]]))
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            elif triplet_sum > 0:
                right -= 1
            else:
                left += 1
    return triplets
```


```python
threesum([2, -1, 1, 0, -2, 7, 2, -3, 4])

```




    [[-3, -1, 4], [-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]




```python
threesum([-1, -1, 0, 1, 2])
```




    [[-1, -1, 2], [-1, 0, 1]]


