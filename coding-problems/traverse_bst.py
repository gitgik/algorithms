"""
Given a binary tree, traverse it, adding the node values into an array,
returning the array.


Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys >= to the node's key.
* Both the left and right subtrees must also be binary search trees.
"""


def in_order_traverse(tree, array):
    """
    Complexity: O(n) time, O(n) space
    NOTE: If we were not storing any array, the space complexity = O(d)
    where d=depth of the longest branch in the BST.
    """
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def pre_order_traverse(tree, array):
    """
    Complexity: O(n) time, O(n) space.
    """
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)
    return array


def post_order_traverse(tree, array):
    """
    Complexity: O(n) time, O(n) space"""
    if tree is not None:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)
    return array
