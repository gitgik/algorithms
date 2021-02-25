### Balanced Tree check
Given a binary tree, check if it is balanced. 


```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def getHeight(root):
    if root is None:
        return -1
    return max(getHeight(root.left), getHeight(root.right)) + 1

def isBalanced(root):
    """O(n log n) time | O(h) space, where h = height of tree."""
    if root is None:
        return True
    
    leftSubtreeHeight = getHeight(root.left)
    rightSubtreeHeight = getHeight(root.right)
    if abs(leftSubtreeHeight - rightSubtreeHeight) > 1:
        return False
    else:
        return isBalanced(root.left) and isBalanced(root.right)
```


```python
node = Node(2)
node.right = Node(4)
getHeight(node)
```




    1




```python
node = Node(2)
node.left = Node(3)
node.right = Node(4)
node.left.left = Node(5)
node.left.left.left = Node(6)
```


```python
isBalanced(node)
```




    False


