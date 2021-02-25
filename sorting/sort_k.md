## Problem
You are given a list of N numbers, in which each number is located at most k places away from its sorted position. For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.

# 1st Approach
A good place to start would be to use the sliding window technique. At each position, we find the minimum of the next *k* elements. If this element is less than the left of the window, we swap them.


```python
def sort(array:list, k:int) -> list:
    for i in range(len(array)):
        low = i
        window = array[i + 1: i + k + 1]
        
        for j, item in enumerate(window, i + 1):
            if item < array[i]:
                low = j
        if array[low] < array[i]:
            array[i], array[low] = array[low], array[i]
    return array
```


```python
array = [2, 1, 3, 4, 1]
k = 3
sort(array, k)
```




    [1, 1, 2, 3, 4]



### Optimal Approach

Since we are iterating over N windows of size k, the time complexity is O(N * k). We also need O(k) space to store the window at any given time.

But the problem requires that we solve it in **O(N log k)** time. We can improve on our solution by using a heap. 

- Place the first K elements in a min-heap.
- For each new element in the list, we add it to the heap, then pop the smallest element from the heap, appending it to our result array
- For the remaining left over elements in the heap, add them from lowest to highest into the results array


```python
import heapq

def sort_k(array:list, k:int) -> list:
    res = []
    heap = []
    
    for i in range(k):
        heapq.heappush(heap, array[i])
    
    for i in range(k, len(array)):
        heapq.heappush(heap, array[i])
        smallest = heapq.heappop(heap)
        res.append(smallest)
    
    while heap:
        res.append(heapq.heappop(heap))
        
    return res
    
    
```


```python
array = [2, 1, 3, 4, 1]
sort_k(array, k=3)
```




    [1, 1, 2, 3, 4]



Since each push and pop overation in a heap takes O(log K) time, and since we are performing each of these operations N times, this algorithm will satisfy our requirement of O(N log K). 

The space complexity will be O(N) because of storing the elements in an auxiliary results array.


```python

```
