## Problem
Write a function that takes a binary tree and returns a list of branch sums (from leftmost node to rightmost node).


```python
"""
The idea is to recursively traverse the tree from the root node to the leaf nodes. 
We'll use a depth-first-traversal and recursively pass the new running sum of previously visited node values to each node you are visiting.
Our base case for the recursion will be if the current node has no left or right child nodes, we know it's a leaf node at the end of a branch.
Simply append the new running sum to the sum list and return.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    """Complexity: O(n) time | O(n) space, 
    where n = number of nodes in binary tree.
    """
    sums = []
    sum_helper(root, 0, sums)
    return sums
    
def sum_helper(current_node, running_sum, branch_sum):
    if current_node is None:
        # Sometimes, there might be a left node but no right node or vice versa. So return.
        return
    
    new_running_sum = running_sum + current_node.value
    # base case
    if current_node.left is None and current_node.right is None:
        branch_sum.append(new_running_sum)
        return
    # recursively work on the left child node and right child node
    sum_helper(current_node.left, new_running_sum, branch_sum)
    sum_helper(current_node.right, new_running_sum, branch_sum)
```


```python
## unit tests
import unittest

class BranchSumTestCase(unittest.TestCase):
    def test_case_0(self):
        tree = BinaryTree(1)
        self.assertEqual(branch_sums(tree), [1])
        
    def test_case_1(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)
        self.assertEqual(branch_sums(tree), [3, 4])
    

# if __name__ == "__main__":
#    unittest.main(argv=[""], exit=False)
        
```


```python

```
