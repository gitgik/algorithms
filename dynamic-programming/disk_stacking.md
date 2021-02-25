### Disk stacking
An array's element represents a disk. Each element has `[length, width, height]`
Write a function that will stack the disks and build a tower with the greatest height, such that each disk has strictly lower dimensions than those below it.

Sample input
```
array = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
```

Sample output:
```
[[4, 4, 5], [3, 2, 3], [2, 1, 2]]

The tower looks something like this

        [2, 1, 2]
       [ 3, 2, 3 ]
      [4,   4,   5]
```



```python
def diskStacking(disks):
    """O(n) space, O(n^2) time"""
    # sort based on height
    disks.sort(key=lambda disk: disk[2])
    diskHeights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    
    # maxHeightIndex
    maxHeightIndex = 0
    
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            # validate dimensions
            if areValidDimensions(otherDisk, currentDisk):
                if diskHeights[i] <= currentDisk[2] + diskHeights[j]:
                    diskHeights[i] = currentDisk[2] + diskHeights[j]
                    sequences[i] = j
        # update maxHeightIndex: which will help us backtrack to find the disks involved.
        if diskHeights[i] >= diskHeights[maxHeightIndex]:
            maxHeightIndex = i
    return buildSequence(disks, sequences, maxHeightIndex)
    
def buildSequence(array, sequences, currentIdx):
    results = []
    while currentIdx is not None:
        results.append(disks[currentIdx])
        currentIdx = sequences[currentIdx]
    return results
        
def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

```


```python
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
diskStacking(disks)
```




    [[4, 4, 5], [3, 2, 3], [2, 1, 2]]




```python

```
