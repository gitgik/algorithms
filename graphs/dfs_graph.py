"""
Depth first search for a graph.
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    for nextVertex in graph[start] - visited:
        dfs(graph, nextVertex, visited)
    return visited


# iterative approach
def dfs_iterative(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


# Class implementation of a graph
class Graph():
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Graph(name))
        return self

    def depth_first_search(self, array):
        """
        Approach: Recursively call each child starting from the root vertex.
        This allows the function to traverse the tree,
        visiting the left-most child first and adding the values to the array

        Complexity: O(V + E) time | O(V) space | V = vertices, E = edges
        """

        array.append(self.name)
        for child in self.children:
            # self = child
            child.depth_first_search(array)
        return array


graph = Graph('A').add_child('B').add_child('C').add_child('Z')
graph.children[0].add_child('D').add_child('E')
graph.children[1].add_child('W').add_child('X')
graph.children[2].add_child('@').add_child('$').add_child('&')

print(graph.depth_first_search(array=[]))
