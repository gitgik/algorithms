"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys >= to the node's key.
* Both the left and right subtrees must also be binary search trees.
"""


def validate_bst(tree):
    """
    Recursive approach to validating a Binary Search Tree.

    Complexity:
        O(n) time, since we are traversing every node once.
        O(d) space, where d == the depth of the binary search tree.
        The depth of the tree is the length of the longest branch.
    """
    return is_valid_helper(tree, min_value=float("-inf"), max_value=float("inf"))

def is_valid_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False

    left_is_valid = is_valid_helper(tree.left, min_value, tree.value)
    return left_is_valid and is_valid_helper(tree.right, tree.value, max_value)
