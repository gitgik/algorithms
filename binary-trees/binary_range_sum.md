### Range sum

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:
```
    5
   / \
  3   8
 / \ / \
2  4 6  10

```
and the range [4, 9], return 23 (5 + 4 + 6 + 8).




```python
class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = value
        
    def insert(self, values, i=0):
        
        if i >= len(values):
            return
        
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = Node(values[i], parent=current)
                break
            queue.append(current.left)
            if current.right is None:
                current.right = Node(values[i], parent=current)
                break
            queue.append(current.right)
                
        self.insert(values, i + 1)
        return self


def range_sum(root, a, b):
    """Complexity
        O(n) space, O(n) time,  where n is number of nodes in the binary tree 
    """
    tree_sum = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if a <= current.value <= b:
            tree_sum += current.value 
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return tree_sum
        
```


```python
# create test node
node = Node(5).insert([3, 8, 2, 4, 6, 10])
node.left.left.value
```




    2




```python
range_sum(node, *[4, 9])
```




    23




```python

```
