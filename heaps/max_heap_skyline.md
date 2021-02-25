## Skyline

The skyline of a city is composed of several buildings of various widths and heights, possibly overlapping one another when viewed from a distance. We can represent the buildings using an array of `(left, right, height)` tuples, which tell us where on an imaginary x-axis a building begins and ends, and how tall it is. The skyline itself can be described by a list of (X, height) tuples. X denotes the location at which the height visible to a distant observer changes, and height is the new height observed at that point.

Given an array of buildings as described above, create a function that returns the skyline.

For example, if the input consists of the buildings 

```python
[(0, 15, 3), (4, 11, 5), (19, 23, 4)]
```

These buildings would create a skyline that looks like the one below:

```
     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------

```

Output:

`[(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]`.

## Approach
For each building we have to compare its height with others that overlap with it. This comparison with each building in the list will lead to a O(N2) runtime. 

To speed it up, we can use a max heap. The max heap will hold at all the buildings that overlap with the current building, and ordered by height.

First step is to order the buildings using their `left` edge values, and use `height` to break any tie. 

For each building:
- Pop all the elements from the heap whose right edge value don't overlap with the current building 
- Push the current building onto the heap
- if the heap max has a different height than the last one in the skyline, we add (left, heap_max_height) to the solution.

Note however that we haven't evaluated the ends of each building (i.e, 15, 11, 23). We can include these points as zero-length "buildings" before we sort them.



```python
import heapq

def skyline(buildings):
    buildings += [(r, r, 0) for (_, r, _) in buildings]
    buildings.sort(key=lambda x: (x[0], -x[2]))
    
    skyline = []
    heap = [(0, float('inf'))]  # (height, right)
    
    for left, right, height in buildings:
        # pop all buildings from heap whose right edge does not overlap with the current building's left edge
        while heap and left >= heap[0][1]:
            heapq.heappop(heap)
        
        # push current building onto the heap
        heapq.heappush(heap, (-height, right))
        
        # if the max in the heap has a different height than the last one in the skyline
        if not skyline or skyline[-1][1] != -heap[0][0]:
            skyline.append((left, -heap[0][0]))  # adds (left, heap_max_height)
            
    return skyline
```


```python
buildings = [(0, 15, 3), (4, 11, 5), (19, 23, 4)]
skyline(buildings)
```




    [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]



After adding the zero-length points, the list of buildings will contain 2N elements, which will take `O(N log N)` time to sort. For each element in the list, we perform one push operation, and possibly several pop operations. Since in total the number of elements that can be popped from or pushed to the heap is 2N, there will be O(N) operations which each take O(log N) time, for an overall time complexity of ***O(N log N)***.

Both the heap and solution array can have no more than 2N elements, so the space required will be ***O(N)***.


```python

```
