```python
### Reverse a linked-list, given the head of the linkedlist. Return the new head.
def reverse(head):
    """Reverse In place. 
    O(1) space | O(n) time, where n = number of nodes in the linked list.
    """
    previous_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    
    # we return the previous node because the current is now None (new tail)
    return previous_node
```


```python

```
