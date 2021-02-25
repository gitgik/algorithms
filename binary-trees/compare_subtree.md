### Problem

Given two non-empty binary trees `s` and `t`, check whether tree t has exactly the same structure and node values with a subtree of `s`. 

A subtree of `s` is a tree consists of a node in `s` and all of this node's descendants. 
The tree `s` could also be considered as a subtree of itself.


```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_subtree(s, t):
    """O(N * M) worst case time, where N is number of nodes in tree s, M is number of nodes in tree t"""
    def is_equal(s, t):
        """O(min(M, N)) time | O(N)"""
        
        if s is None and t is None:
            return True
        # The base case: handle an empty subtree
        if s is None or t is None:
            return False
        if s.value != t.value:
            return False
        return is_equal(s.left, t.left) and is_equal(s.right, t.right)
    
    if s is None:
        return False
    if is_equal(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)
```


```python
t = Node(1, Node(2, Node(4), Node(5)), Node(3))
s = Node(11, Node(7, t))
```


```python
is_subtree(s, t)
```




    True




```python
def isSubtree(s, t):
    """O(M + N) time | O(N) space"""
    def preorder(root):
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                traversal.append('.')
                continue
            else:
                traversal.append(str(node.value))
            stack.append(node.right)
            stack.append(node.left)
        return ''.join(traversal)
    
    s = preorder(s)
    t = preorder(t)
    return t in s
```


```python
isSubtree(s, Node(1))
```




    False




```python
isSubtree(s, t)
```




    True


