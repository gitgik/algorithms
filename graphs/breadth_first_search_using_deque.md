### Breadth First Search
Given a hashtable containing vertices as keys and values as each vertex's corresponding neighbors, write a function that takes in a starting vertex and determines if a given vertex exists in the graph. Return True if found, else False.

```
Sample input:

Find if vertex W exists, starting with vertex G.

         G ––– F
          \   / 
            A  –– E
           /  \    |
         X ––  W –– Q
 
 Sample output: True
 ```


```python
from collections import deque

def search(hashmap, start, needle):
    """O(v + e) time | O(v) space, where v = vertices and e = edges."""
    search_queue = deque()
    search_queue += hashmap[start]
    visited = []
    while search_queue:
        vertex = search_queue.popleft()
        if not vertex in visited:
            if vertex == needle:
                return True
            else:
                visited.append(vertex)
                search_queue += hashmap[vertex]
    return False
```


```python
# Create the graph
graph = {
    'G': ['A', 'F'],
    'A': ['X', 'W', 'E'],
    'F': ['A'],
    'X': ['W'],
    'W': ['Q'],
    'E': ['Q'],
    'Q': []
}

search(graph, "G", "W")
```




    True


