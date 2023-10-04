## Remove all consecutive nodes that sum to zero
Given a linked list, remove all consecutive nodes that sum to zero. 
Print out the remaining nodes.

Example:
    Given the input 2 -> 3 -> -5 -> 7 -> -1 -> 1,
    
    Remove 2 -> 3 -> -5, then remove -1 -> 1, leaving 7
    



```python
class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
```


```python
def print_node(ll):
    start = end = ll
    
    while start:
        end = start
        total = 0
        skip = False
        
        while end:
            total += end.data
            if total == 0:
                start = end
                skip = True
                break
            end = end.next
        
        if not skip:
            print(start.data)
        start = start.next
```


```python
ll = LinkedList(2, next=LinkedList(3, next=LinkedList(-5, next=LinkedList(7, next=LinkedList(-1, next=LinkedList(1))))))
```


```python
print_node(ll)
```

    7


### Solution explanation
The key information here is that the nodes that sum to zero must be consecutive.
We can therefore solve this using two-pointer approach.

1. Both our start and end pointer will be at the head of our linked list. 
2. The end node will traverse the list. While doing so, we add each successive value to a running total sum.
3. If at a point the total adds to zero, we know that we shouldn't print these nodes. Therefore, we advance the start pointer past each of them and continue the process.
4. For a given start node, if we're able to traverse all reamining nodes without summing to zero, that node must be part of the solution. Once we print the value of the node, we advance the start pointer one node forward and repeat.

In the worst case, we must move our end pointer across the remainder of the linked list for each potential start node, taking O(N<sup>2</sup>). Total space required is O(1) since at any given point we are only tracking the two pointers and our running total sum


```python

```
