"""Invert a binary tree.

The function should swap every left node with its corresponding(mirrored) right node.
Each node in the tree has a value stored in a property called 'value', and two child nodes
stored in propeties 'left' and 'right'. Children nodes can either be nodes Binary Tree
nodes themselves or None values.


Sample input:
    1
   / \
  2   3
 | \
 4  5

Sample output:
    1
   / \
  3   2
     / \
    5   4
"""


def invert_binary_tree(tree):
    """Recursive implementation of inverting a binary search tree.

    Complexity:
        O(n) time, where n = number of nodes in binary tree.
        O(d) space, where d = depth of binary tree. (the depth is simply the longest
        branch of the tree)
    """
    if tree is None:
        return
    swap_left_right(tree)
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)


def invert_binary_tree_iteratively(tree):
    """Iterative approach to inverting a binary tree.

    Complexity:
        O(n) time, O(n) space
    """
    queue = [tree]

    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        else:
            swap_left_right(current)
            queue.append(current.left)
            queue.append(current.right)


def swap_left_right(tree):
    tree.left, tree.right = tree.right, tree.left
