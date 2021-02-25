### Min-Heap construction
Implement a min-heap class that support:
    - building a min-heap from an array of integers.
    - inserting values into the heap
    - removing the root of the heap
    - peeking the root of the heap
    - siftig up through the heap (used when adding a new value)
    - sifting down through the heap (used to rearrange the heap to form a min-heap)
    
Represent the min-heap as an array. So given an input array, create the min-heap **inplace**.


```python
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    
    def buildHeap(self, array):
        """O(n) time | O(1) space, where n = number of elements in input array."""
        lastParentIndex = (len(array) - 2) // 2
        for currentIndex in reversed(range(lastParentIndex + 1)):
            self.siftDown(currentIndex, len(array) - 1, array)
        return array
    
    def siftDown(self, currentIdx, endIdx, heap):
        """O(log n) time | O(1) space"""
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            if currentIdx * 2 + 2 <= endIdx:
                childTwoIdx = currentIdx * 2 + 2
            else:
                childTwoIdx = -1
                
            if childTwoIdx != -1 and childTwoIdx < childOneIdx:
                indexToSwap = childTwoIdx
            else:
                indexToSwap = childOneIdx
            
            if heap[indexToSwap] < heap[currentIdx]:
                self.swap(currentIdx, indexToSwap, heap)
                # update the new current index
                currentIdx = indexToSwap
                # get the new child for this new currentIdx, if any
                childOneIdx = currentIdx * 2 + 1
            else:
                return
    
    def siftUp(self, currentIdx, heap):
        """O(log n) time | O(1) space"""
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[parentIdx] < heap[currentIdx]:
            self.swap(parentIdx, currentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
    def insert(self, value):
        """O(log n) time | O(1) space"""
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
    
    def remove(self):
        """O(log n) time | O(1) space"""
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
    
    def peek(self):
        """O(1) time | O(1) space"""
        return self.heap[0]
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
```


```python
minheap = MinHeap([23, 45, 10, -3, 4, 16, 20, 7])
minheap.peek()
```




    -3




```python

```
