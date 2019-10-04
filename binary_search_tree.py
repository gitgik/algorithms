"""BST implementation.

A node is said to be a BST node if and only if it satisfies the BST property:
    its value is greater than all the node values to its left; its values is less than or
    equal to the values of every node to its right, and all its children nodes are either
    BST nodes themselves or null values.

    The BST shuold support insertion, searching and removal of values.
    The removal method should only remove the first instance of the target value.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def contains(self, value):
        """Search for a value in the BST.
        """
        current_node = self
        if value < current_node.value:
            current_node = current_node.left
        elif value > current_node.value:
            current_node = current_node.right
        else:
            # found it!
            return True
        return False
