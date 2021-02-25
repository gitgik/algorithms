```python
"""Breadth-first search implementation.

Given a Node class that has a name, and an array of optional children nodes to form
a tree-like structure.
Implement a method in the class which takes in an empty array,
traverses the tree using the Breadth-first Search approach
(specifically navigating the tree left to right),
Store all the nodes it traverses in the input array, and returns it.

Sample input:
    A
   / \
  B   C
 / \
D   E
   / \
  F   G


Sample output: [A,B,C,D,E,F,G]
"""


class Node:

    def __init__(self, name):
        self.name = name
        self.children = []


    def add_child_nodes(self, name):
        self.children.append(Node(name))
        return self

    def breadth_first_search(self, array):
        """
        Complexity:
            O(v + e) time, where v = vertices(nodes) and e = edges(connections)
            O(v) space, since we at worst case, we have a queue that holds V - 1 nodes.
        """
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array

```


```python

```
