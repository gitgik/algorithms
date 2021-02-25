```python
"""
Given a binary tree, print the nodes level-wise. For example:
  1
 / \
2   3
   / \
  4   5
   should print 1, 2, 3, 4, 5.
"""

from queue import Queue


class Node():
    def __init__(self, value, left=None, right=None):
        """Initialize the node's properties.'"""
        self.value = value
        self.left = left
        self.right = right


def print_node_values(tree):
    """use a queue to print the values, and continuously add the child elements,
    starting with the left, then the right child to the back of the queue.
    Eventually, the queue gets smaller, printing the FIFO value it pops, until empty.

    Time and Space Complexity: O(n), since we have to look at the whole tree.
    """
    queue = Queue()
    queue.put(tree)

    while not queue.empty():
        node = queue.get()
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
        print(node.value)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_node_values(root)
```

    1
    2
    3
    4
    5



```python

```
