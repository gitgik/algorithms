## Recursive problems around trees

### 1. Finding tree height
Given a binary tree, find the max-height of the tree. The height of a tree is the number of edges on the longest path from the root to the leaf.

For example given the following tree,

```
      2
     / \
    3   5
   /   / \
  4   6   7
```

Return `3`


```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1

t = Node(
    value=2, 
    left=Node(3, Node(4)), 
    right=Node(5, Node(6), Node(7))
)
height(t)
```




    3



### 2. Return nodes at a given level
Given a binary tree, return the value of the nodes at a given level. In other words, breadth-first search at a given level.

For example given the following tree,

```
      1
     / \
    2   3
   /\   /\
  4  5 6  7
  
  level = 2
```

Return `[4, 5, 6, 7]`


```python
def bfs_at_level(tree, level, visited=[]):
    if tree is None:
        return
    
    if level == 1:
        visited.append(tree.value)
    elif level > 1:
        bfs_at_level(tree.left, level - 1, visited)
        bfs_at_level(tree.right, level - 1, visited)
    return visited

tree = Node(
    value=1, 
    left=Node(2, Node(4), Node(5)), 
    right=Node(3, Node(6), Node(7))
)
bfs_at_level(tree, level=3)
```




    [4, 5, 6, 7]



### 3. Depth-first traversals 
Given a tree, traverse the tree in an in-order, pre-order and post-order fashion. Return the node values in a list.


```python
def inOrderTraversal(node, results=[]):
    """Visit left-most child, then root, then right"""
    if node is None:
        return
    inOrderTraversal(node.left)
    results.append(node.value)
    inOrderTraversal(node.right)
    return results

def preOrderTraversal(node, results=[]):
    """Visit root first, then left, right"""
    if node is None:
        return
    results.append(node.value)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
    return results

def postOrderTraversal(node, results=[]):
    if node is None:
        return
    postOrderTraversal(node.left, results)
    postOrderTraversal(node.right, results)
    results.append(node.value)
    return results
```

The tree above looks like this

```
     2
    / \
   3   5
  /    /\
 4    6  7
```


```python
tree = Node(
    value=2, 
    left=Node(3, Node(4)), 
    right=Node(5, Node(6), Node(7)))
print(f'In-order => {inOrderTraversal(tree)}')
print(f'Pre-order => {preOrderTraversal(tree)}')
print(f'Post-order => {postOrderTraversal(tree)}')

```

    In-order => [4, 3, 2, 6, 5, 7]
    Pre-order => [2, 3, 4, 5, 6, 7]
    Post-order => [4, 3, 6, 7, 5, 2]


### 4. Sum of depths. 
Given the root of a binary tree, find the sum of all its depths.

For example give the tree:

```
       1
      / \
     2   3
    /\   /\
   4  5 6  7
  /\
 8  9
```

Returns:
```
16
```


```python
def dfs_helper(node, depth, result=0):
    result += depth
    if node.left is not None:
        result += dfs_helper(node.left, depth + 1)
    if node.right is not None:
        result += dfs_helper(node.right, depth + 1)
    return result
        
def sum_depths(root):
    return dfs_helper(root, depth=0)
```


```python
tree = Node(
    1, 
    Node(2, Node(4, Node(8), Node(9)), Node(5)), 
    Node(3, Node(6), Node(7))
)
sum_depths(tree)
```




    16



### 5. Sum up all the depths of each node in a binary tree. 

Given the following tree:
    
```
   
       1
      / \
     2   3
    /\   /\
   4  5 6  7
  /\
 8  9
 
 Return 26 ==> (1 has 16, 2 has 6, 3 and 4 have 2 each) = 26
```

### Approach 
A straightforward approach is to use the method above to find the depths each node's subtree and sum them up.


```python
 def dfs_helper(node, depth, result=0):
    result += depth
    if node.left is not None:
        result += dfs_helper(node.left, depth + 1)
    if node.right is not None:
        result += dfs_helper(node.right, depth + 1)
    return result

def sum_depths_all_nodes(node):
    stack = [node]
    total = 0
    while stack:
        current_root = stack.pop(0)
        total += dfs_helper(current_root, depth=0)
        if current_root.left is not None:
            stack.append(current_root.left)
        if current_root.right is not None:
            stack.append(current_root.right)
    return total
```


```python
root = Node(
    1, 
    Node(2, Node(4, Node(8), Node(9)), Node(5)), 
    Node(3, Node(6), Node(7))
)
sum_depths_all_nodes(root)
```




    26



### Optimal approach
The bottom-down recursive approach above is very inefficient because of the bottom down approach. Since we begin from the root, we are bound to repeatedly compute the depths of nodes already encountered as we go down the tree.

To speed things up, we can use a bottom-up approach. We'll use a pair of total number of nodes in a subtree and it's respective depth to calculate the total sum.
For each leaf node, the pair is `(1, 0)` since the nodes in their subtree is only one. And they don't have a depth, so zero.

We'll recursively work up, adding the child pair node values to the depth value of their parents. 
Finally, we return the total in a global variable.




```python
global result
result = 0
def bottom_up_dfs(node):
    # pair.first = the number of nodes in a subtree
    # pair.second = the sum of depths of that subtree
    pair = [1, 0]
    
    if node.left is not None:
        child_pair = bottom_up_dfs(node.left)
        pair[1] += child_pair[1] + child_pair[0]
        pair[0] += child_pair[0]
        
    if node.right is not None:
        child_pair = bottom_up_dfs(node.right)
        pair[1] += child_pair[1] + child_pair[0]
        pair[0] += child_pair[0]

    global result
    result += pair[1]
    
    return pair[0], pair[1]
    
def rooted_depths(node):
    bottom_up_dfs(node)
    return result
    
```


```python
bintree = Node(
    1, 
    Node(2, Node(4, Node(8), Node(9)), Node(5)), 
    Node(3, Node(6), Node(7))
)
rooted_depths(bintree)
```




    26




```python

```
