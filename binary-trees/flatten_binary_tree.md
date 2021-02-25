## Flatten Binary Tree
Write a function that takes in a binary tree, flatten it, and returns the left-most node.

Sample input:
```
tree =   1
        /  \
       2    3
     / \   /
    4   5  6
       / \
      7   8
```

Sample output:
```python
4 <-> 2 <-> 7 <-> 5 <-> 8 <-> 1 <-> 6 <-> 3
```



```python
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorderTraversal(root, array):
    if root is not None:
        inorderTraversal(root.left, array)
        array.append(root)
        inorderTraversal(root.right, array)
    return array

def flattenBinaryTree(root):
    """We in-order traverse the tree and save the values in an array. 
    Then we create the structure and return left-most node"""
    array = inorderTraversal(root, [])
    for i in range(0, len(array) - 1):
        leftNode = array[i]
        rightNode = array[i + 1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return array[0]
```


```python
def flattenTree(root):
    """O (n) time | O(d) space, where d = depth of tree (because of the recursive calls on the callstack)
    If the tree is a balanced binary tree, then it runs on O(log(N)) space.
    """
    leftMostNode, _ = flatten(root)
    return leftMostNode
    
    
def flatten(node):
    # get the left most node and right most node of our current subtree
    
    # base case: The left leaf node is the left most node, rooted at itself
    if node.left is None:
        leftMost = node
    else:
        leftMostLeftSubtreeNode, rightMostLeftSubtreeNode = flatten(node.left)
        # update left and right pointers
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost
    
    # base case: The right leaf node is the right most node, rooted at itself
    if node.right is None:
        rightMost = node
    else:
        leftMostRightSubtreeNode, rightMostRightSubTreeNode = flatten(node.right)
        connectNodes(node, rightMostRightSubtreeNode)
        rightMost = rightSubtreeRightMost
    
    
    return [leftMost, rightMost]

def connectNodes(leftNode, rightNode):
    leftNode.right = rightNode
    rightNode.left = leftNode
```


```python

```
