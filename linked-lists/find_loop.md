### Looped linked list
Write a function that takes in the head of a linked list and returns the node from which the loop originates, in constant space.

Sample input:
```
1 -> 2 -> 3 -> 4
          ^     V
          6 <-  5
```

Sample output:
```
3 -> 4
|    |
6 <- 5
```


```python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    """Use two pointers: Traverse the list with one iterating once, and the other jumping one node. 
    They eventually overlap at a point D, where the distance is equivalent to start of the list to the point where the loop is.
    We can therefore obtain that loop point by taking the first pointer back to the head, then iterating both pointers one step until they converge at that point.
    
    Time: O(n) | Space: O(1), where n = number of nodes in linked list"""
    first = head.next
    second = head.next.next
    
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
```


```python

```
