### Problem
Given the root of a Binary Search Tree, find its diameter.

Sample input:

```
         10
       /   \ 
      5     15
     / \     \
    2   5    22
   /
   1
```

Expected output:

```
6 => (We get 6 from counting 1, 2, 5, 10, 15, 22)
```

### Solution
The diameter of a tree T is the largest (max) of the following quantities:

- the diameter of T’s left subtree.
- the diameter of T’s right subtree.
- the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)


```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    # base case: tree is empty
    if root is None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))
```


```python
bst = Node(6, Node(3, Node(1), Node(4, Node(2))), Node(8, Node(7), Node(9)))
```


```python
diameter(bst)
```




    6


