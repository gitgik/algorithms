### Remove a node in a Binary Search Tree.

Given a Binary search tree (BST), remove a node from the tree.
Each BST node has a `value`, a `left` node and a `right` node

A node is said to be a valid BST if it meets the following requirements:
    1. Its value is strictly > than the value of every node to its left,
    2. Its value is less than or equal to every node to its right,
    3. Its children nodes are either valid BST nodes or null.




```python
class BST:
    def __init__(self, value):
        self.value = value
        self.left = left
        self.right = right
        
    def remove(self, value, parent_node):
        """Complexity:
            Average: O(log (n)) time, O(1) space, where n is the total number of nodes in the tree
            Worst case: O(n) time, O(1) space
        """
        current = self
        
        while current is not None:
            if value < current.value:
                parent_node = current
                current = current.left
            elif value > current.value:
                parent_node = current
                current = current.right
            else:
                # first subcase: found the node, (value == current.value)
                if current.left is not None and current.right is not None:
                    # go ahead and find the smallest node in the right subtree to replace the current node
                    current.value = current.right.get_min_value()
                    # delete the node that we got the min value from
                    current.right.remove(current.value, parent_node=current)
                # second subcase: we are removing the root node
                elif parent_node is None:
                    # At this point, the root node we want to remove has only one branch: left or right.
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    elif current.right is not None:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        # The tree has a single node. Do nothing.
                        pass
                elif parent_node.left == current:
                        parent_node.left = current.left if current.left is not None else current.right
                elif parent_node.right == current:
                        parent_node.right = current.left if current.left is not None else current.right
                # we've found the value, lets just break
                break
        return self
    
    def get_min_value(self):
        node = self
        while node.left is not None:
            node = node.left
        return node.value
                

```
