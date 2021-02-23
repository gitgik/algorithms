## Problem
Write a function to find the closest value in the BST to a given target integer.

The BST contains BST nodes. Each node stores an integer in a property called "value", and
two children in properties called "left" and "right".

A Node is said to be a BST node if and only if it satisfies the following property:
- Its value is greater than the nodes values to its left,
- Its value is less than or equal to the node values to its right
- Both its children are either BST nodes or None values.


We'll define the BST and the function that finds the closest value to the target integer
contained in the BST.

Sample Input:

```
    10      Target: 12
    /  \
    5    15
   / \   |  \
  2  5  13   22
 /        \
1          14

```

Output: `13`


```python
import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


def findClosestValueInBst(tree, target):
    """
    First start with infinity as the closest value to the target,
    so that we have something to compare to the
    absolute value difference of (first node - target)
    """
    closest = math.inf
    root = tree
    while root is not None:
        if root.value == target:
            return root.value

        if abs(root.value - target) < abs(closest - target):
            closest = root.value

        if root.value < target:
            root = root.right
        elif root.value > target:
            root = root.left
        else:
            break
    return closest
```


```python
bst = BST(10).insert(5).insert(2).insert(5).insert(1).insert(5).insert(15) \
    .insert(13).insert(14).insert(22)

findClosestValueInBst(bst, 12)
```




    13




```python

```
