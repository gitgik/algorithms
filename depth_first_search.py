"""
Implementation of depth first search on a tree.
"""


class Node():
    def __init__(self, name):
        self.name = name  # node value
        self.children = []  # optional child nodes

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        """
        Approach: Recursively call each child starting from the root vertex.
        This allows the function to traverse the tree,
        visiting the left-most child first and adding the values to the array

        Running Complexity:
            Time: O(V + E), where V = number of vertices, E = edges
            Space: O(V)
        """

        array.append(self.name)
        for child in self.children:
            # self = child
            child.depth_first_search(array)
        return array


test = Node('A').add_child('B').add_child('C').add_child('Z')
test.children[0].add_child('D').add_child('E')
test.children[1].add_child('W').add_child('X')
test.children[2].add_child('@').add_child('$').add_child('&')

print(test.depth_first_search(array=[]))
