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

    def insert(self, value):
        """Insert a value in the BST.

        Complexity:
            Average Case:
                O(log(N)) time
                O(1) space

            Worst Case: (Where the tree is unbalanced and has only one branch to the left)
                O(n) time
                O(1) space
        """
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                # value is greater than current node's value
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

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
