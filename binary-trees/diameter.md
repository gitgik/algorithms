# Binary Tree Diameter
Find the diameter of a given binary tree. The diameter of a binary tree is the longest path, even if the path doesn't go through the root.

```
          1
         / \
        6   2
       / \   
      5   7 
     / \    \
    4   3    8
              \
              9
```
returns 5  (4 -> 5 -> 6 -> 7 -> 8 -> 9)

### Approach
The diameter of a binary tree is equal to:
    
```
max(longest path through root, left diameter, right diameter)

the longest path through the root = left height + right height
```

So we'll traverse each node until the we hit the leaf nodes. Once this happens, we recursively build up the diameter and height of each child node, which adds up the the diameter and height of their parent node above them, until we get to the root.
We'll return the maximum diameter based on the formula above.



```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def find_diameter(root) -> int:
    if root is None:
        return 0
    
    height_left = height(root.left)
    height_right = height(root.right)
    
    d_left = find_diameter(root.left)
    d_right = find_diameter(root.right)
    
    return max(height_left + height_right, max(d_left, d_right))
    
def height(node) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
```


```python
root = Node(1, left=Node(2, Node(4, Node(5))), right=Node(3, None, Node(6)))
find_diameter(root)
```




    5



The time complexity will be **O(N)** since we are visiting each node once. The space complexity will be **O(N)** because we are storing N recursive calls on the call stack.


```python

```
