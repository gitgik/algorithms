"""
Given a binary tree, determine if it is a valid binary search tree (BST).

A BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.
"""

class TreeNode:
    def __init__(key):
        self.key = key
        self.left = None
        self.right = None

        
def is_bst(root):
    return is_bst_helper(root, min_value=float("-inf"), max_value=float("inf"))

def is_bst_helper(root, min_value, max_value):
    """ O(n) time | O(d) space, where d == the depth of the binary search tree."""
    if root is None:
        return True
    if root.value <= min_value or root.value >= max_value:
        return False

    left_is_valid = is_bst_helper(root.left, min_value, root.key)
    return left_is_valid and is_bst_helper(root.right, root.value, max_value)
