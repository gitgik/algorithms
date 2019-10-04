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
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                # found it!
                return True
        return False

    def remove(self, value, parent_node = None):
        """Remove a node from the BST tree."""
        current_node = self
       while current_node is not None:
           if value < current_node.value:
               parent_node = current_node
               current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                # we've found the node, time to delete it
                if current_node.left is not None and current_node.right is not None:
                    # set current node value = smallest value of right subtree.
                    current_node.value = current_node.rigth.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    # if we are removing the root node (it does not have a parent node)
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.rigtht
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # no child nodes exist for this BST, so we just delete the BST
                        current_node.value = None
                elif parent_node.left == current_node:
                    parent_node.left =
                        current_node.left if current_node.left is not None else
                        current_node.right
                elif parent_node.right == current_node:
                    parent_node.right =
                        current_node.right if current_node.right is not None else
                        current_node.left
                break
        return self

    def get_min_value(self):
        """Helper function to find the smallest value of a sub-tree."""
        current_node = self
        while current_node.value is not None:
            current_node = current_node.left
        return current_node.value

