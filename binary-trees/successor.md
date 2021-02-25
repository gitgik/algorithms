## Node's successor

Given a binary tree and a node in the tree, find the successor of the node.

A node's successor is the next node when traversing a binary tree in an in-order fashion.

For example given the following tree:
```
         1
        / \
       2   3
      /\
     4  5
    / 
   6
```
Return 1, since 1 follows 5 in when arranged in-order.
    



```python
class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        

def findSuccessor(tree: Node, node: Node) -> Node:
    # if node has right child, find the left most node under it: that's our successor
    if node.right is not None:
        return getLeftMostChild(node.right)
    return getRightMostParent(node)

def getLeftMostChild(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def getRightMostParent(node):
    current = node.parent
    while current.parent is not None and current.parent.right == current:
        current = current.parent
    return current.parent
```


```python
root = Node(1)
root.left = Node(2)
root.left.parent = root
root.right = Node(3)
root.right.parent = root

root.left.left = Node(4)
root.left.left.parent = root.left
root.left.right = Node(5)
root.left.right.parent = root.left
root.left.left.left = Node(6)
root.left.left.left.parent = root.left.left

# input node to find its successor 
node = root.left.right
findSuccessor(root, node).value
```




    1




```python

```
