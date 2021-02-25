## Problem
Write a function that takes in the head of a singly linked list, and an integer k (assume the list has at least k nodes). The function should remove the kth node from the end of the list.

Every node has a value property to store its value and a next property to point to the next node in the linked list.

Sample input: 1 -> 2 -> 3 -> 4 -> 5, 2
Sample output: 1 -> 2 -> 3 -> 5


```python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_kth_node_from_end(head, k):
    # Space: O(1) | Time: O(n) 
    counter = 1
    first = head
    second = head
    
    while counter <= k:
        second = second.next
        counter += 1
    
    if second is None:
        # we're removing the head (first node)
        head.value = head.next.value
        head.next = head.next.next
    
    while second.next is not None:
        first = first.next
        second = second.next
    # remove the kth node by skipping it (garbage collected)
    first.next = first.next.next
```


```python
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def add_many(self, values):
        # utility function to add many values in a linked list
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    
    def get_nodes_in_array(self):
        current = self
        nodes = []
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
```


```python
li = LinkedList(0).add_many([1, 2, 3, 4, 5, 6, 7])
remove_kth_node_from_end(li, 4)
li.get_nodes_in_array()
```




    [0, 1, 2, 3, 5, 6, 7]




```python
# feel free to run these unit tests 
import unittest

class TestLinkedListKthRemoval(unittest.TestCase, LinkedList):  
    def test_case_0(self):
        linked_list = LinkedList(0).add_many(list(range(1,9)))
        result = LinkedList(0).add_many(list(range(1, 8)))
        remove_kth_node_from_end(linked_list, 1)
        self.assertEqual(linked_list.get_nodes_in_array(), result.get_nodes_in_array())
        
    def test_case_1(self):
        test = LinkedList(0).add_many([1, 2, 3, 4, 5, 6, 7, 8, 9])
        remove_kth_node_from_end(test, 2)
        expected = LinkedList(0).add_many([1, 2, 3, 4, 5, 6, 7, 9])
        self.assertEqual(test.get_nodes_in_array(), expected.get_nodes_in_array())
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```


```python

```
