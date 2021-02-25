### The Problem
Write a function that returns the youngest common ancestor to the two descendants in a tree.

Sample Input:
```
     A
    / \
   B   F
  / \   \
 G   C   S
     |
     D
 
 topAncestor = node A
 descendantOne = node G
 descendantTwo = node D
```
Sample output:
```
Node B
```


```python
# solution
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    """
    First, get the depth of each descendant node, then get the difference. Backtrack the lower node to come to the same level
    as the higher node. Then, backtrack both nodes in tandem to find their next common parent.

    O(d) time | O(1) space, where d == depth of tree.
    """
    dOneDepth = getDepth(descendantOne, topAncestor)
    dTwoDepth = getDepth(descendantTwo, topAncestor)

    if dOneDepth > dTwoDepth:
        diff = dOneDepth - dTwoDepth
        return backtrackTree(descendantOne, descendantTwo, diff)
    else:
        diff = dTwoDepth - dOneDepth
    return backtrackTree(descendantTwo, descendantOne, diff)

def getDepth(node, topAncestor):
    """Returns the depth of a node."""
    depth = 0
    while node != topAncestor:
        depth += 1
        node = node.ancestor
    return depth

def backtrackTree(lowerDescendant, higherDescendant, diff):
    """Takes in the descendants and their difference in depth, and uses that to backtrack to a common ancestor."""
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1

    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor

    return lowerDescendant
```


```python

```
