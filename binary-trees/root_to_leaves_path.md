### Problem
Given a binary tree, write a function that returns all possible paths from the root to the leaves.

For example given the following tree

```
    1
   / \
  2   3
     / \
    4   5
```
The paths are
```python
[ [1, 2], [1, 3, 4], [1, 3, 5] ]
```


```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        if left:
            left.parent = self
        if right:
            right.parent = self
        
    def path(self):
        current = self
        path = []
        while current:
            path = [current.value] + path
            current = current.parent
        return path
```


```python
root = Node(
    value=1, 
    left=Node(2), 
    right=Node(3, Node(4), Node(5)))
```


```python
def find_leaves(node):
    paths = []
    queue = list()
    queue.append(node)
    while len(queue):
        node = queue.pop()
        if not node.left and not node.right:
            paths += [node.path()]
            continue
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return paths
```


```python
find_leaves(root)
```




    [[1, 2], [1, 3, 4], [1, 3, 5]]




```python

```
