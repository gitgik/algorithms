### Find second largest node in BST

Given the root to a binary search tree, find the second largest node in the tree.


```python

def find_node(root):
    """Complexity
        O(log(n)) time, where n is total number of nodes in BST
        O(1) space
    """
    current = root
    if current.right is None:
        if current.left is not None:
            return current.left.value
        else:
            # we have a single node BST. There's no other second value to return
            return None
    else:
        while current.right is not None:
            if current.right.right is None:
                second_largest = current.value
                break
            else:
                current = current.right
        return second_largest
```


```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

bst = BSTNode(10)
bst.left = BSTNode(5)
bst.right = BSTNode(12)
bst.right.left = BSTNode(11)
bst.right.right = BSTNode(14)

find_node(bst)
```




    12




```python
# second case (for when the tree only has left subtree)
bst2 = BSTNode(7)
bst2.left = BSTNode(6)
bst2.left.left = BSTNode(5)

find_node(bst2)
```




    6




```python

```
