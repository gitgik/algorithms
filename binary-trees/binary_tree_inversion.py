"""Invert a binary tree.

The function should swap every left node with its corresponding(mirrored) right node.
Each node in the tree has a value stored in a property called 'value', and two child nodes
stored in propeties 'left' and 'right'. Children nodes can either be nodes Binary Tree
nodes themselves or None values.

"""


def invert_binary_tree(tree):
    """Recursive implementation of inverting a binary search tree.

    Complexity:
        O(n) time, where n = number of nodes in binary tree.
        O(d) space, where d = depth of binary tree.
    """
    if tree is None:
        return
    swap_left_right(tree)
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)


def swap_left_right(tree):
    tree.left, tree.right = tree.right, tree.left
