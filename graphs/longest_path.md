## Longest path in a weighted tree

Given a tree where each edge has a weight, compute the longest path in the tree.

For example, given the following tree:

```
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
 ```
and the weights: 
```
a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1

```
the longest path would be `c -> a -> d -> f`, with a length of 17.

Note: The path does not have to pass through the root, and each node can have any amount of children.

## Solution

There are two cases: either the path goes through the root or it doesnt.

If it goes through the root, we can obtain the longest path by combining the two highest heights of the roots' children.
If it doesn't, then we need to look at the longest path of any of the root's children.(remember each node can have many children)

Base Case: Look at a node with no children, in which case the path is 0.
We'll recursively check the longest height and path of each child and keep track of the longest path, updating it when we find a longer path.
At the end, we'll find the max between the longest subpath and the two longest paths of the roots children that can be combined to make a larger path. 


```python
from math import inf

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def longest_path(root):
    height, path = longest_height_and_path(root)
    return path

def longest_height_and_path(root):
    longest_path_so_far = -inf
    heighest, second_highest = 0, 0
    
    for length, child in root.children:
        height, longest_path_length = longest_height_and_path(child)
        longest_path_so_far = max(longest_path_so_far, longest_path_length)
        
        
        if height + length > highest:
            highest, second_highest = height + length, highest
        elif height + length > second_highest:
            second_highest = height + length
    return highest, max(longest_path_so_far, highest + second_heighest)
        
        
```

Since we are visiting each node, the solution runs at O(N) time and O(h) space.


```python

```
