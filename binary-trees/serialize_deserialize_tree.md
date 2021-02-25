Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(string)`, which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

```


```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

def serialize(root):
    if root is None:
        return "#"
    return f"{root.value} {serialize(root.left)} {serialize(root.right)}"

def deserialize(s):
    def helper():
        val = next(vals)
        if val == "#":
            return None
        node = Node(val)
        node.left= helper()
        node.right = helper()
        return node
    
    vals = iter(s.split())
    return helper()
```


```python
node = Node('root', Node('left'), Node('right'))
serialize(node)
```




    'root left # # right # #'




```python
deserialize(serialize(node)).right.value
```




    'right'


