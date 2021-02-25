## Problem
Traverse a binary tree in an in-order fashion in constant space. In other words, do it iteratively

Sample input:
```text
            1
           / \
          2   3
         / \
        4   5
        
```   
Sample output: `[4, 2, 5, 1, 3]`


```python
"""
Solution:
    - Try to keep track of the previous node, the current and the next node to be traversed. 
    - If the current node left node is not None, we'll go down and make the next node == current node left child
    - Else, we'll do a callback on the current node.
    - If the previous node is equal to the current node's left node, append current node value to results.
    - Compute the next node: it should be the current node right child if not None or the current node's parent.
"""

def iterative_inorder(tree):
    """Complexity: O(n) time, O(1) space, where n is the number of nodes in the tree."""
    current_node = tree
    prev_node = None  # the previous node
    results = []
    
    while current_node is not None:
        if prev_node is None or prev_node == current_node.parent:
            if current_node.left is not None:
                next_node = current_node.left
            else:
                results.append(current_node.value)
                next_node = current_node.right if current_node.right is not None else current_node.parent
        elif prev_node == current_node.left:
            results.append(current_node.value)
            next_node = current_node.right if current_node.right is not None else current_node.parent
        else:
            # same as elif prev_node == current_node.right
            # we move back up to the parent of the current node, since we are at a right-most node
            next_node = current_node.parent
        
        # update the previous node to be the current node,
        # update current node to be the next node
        prev_node = current_node
        current_node = next_node
    
    return results
    
```


```python
class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        
    
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(value=values[i], parent=current)
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(value=values[i], parent=current)
                break
            queue.append(current.right)
            
        self.insert(values, i + 1)
        return self
```


```python
tree = BinaryTree(1).insert([2, 3, 4, 5])
iterative_inorder(tree)
```




    [4, 2, 5, 1, 3]




```python
# this is the recursive way of doing an in-order traversal -> O(N) time and space
def inOrderTraversal(root, nodes=[]):
    if root is None:
        return None
    inOrderTraversal(root.left)
    nodes.append(root.value)
    inOrderTraversal(root.right)
    
    return nodes
```


```python
inOrderTraversal(tree)
```




    [4, 2, 5, 1, 3]




```python

```
