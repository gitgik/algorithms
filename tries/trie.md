```python
# Implementation of a trie
from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False
    
    def __repr__(self):
        return f'{self.children.keys()}'

class Trie():
    def __init__(self):
        """Initialize variables."""
        self.root = self.get_node()

    def get_node(self):
        """Get the node from the trie."""
        return TrieNode()

    def get_index(self, character):
        """Get the index of a node in the trie.
        """
        return ord(character) - ord('a')

    def insert(self, word):
        """Insert a word into the trie."""
        root = self.root
        for i in range(len(word)):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        root.terminating = True

    def search(self, word):
        """Search for a word in the trie."""
        root = self.root
        print(f'Root:{root}')
        for i in range(len(word)):
            index = self.get_index(word[i])

            if not root:
                return False
            root = root.children.get(index)
            print(f'<<<<{root}')
        return True if root and root.terminating else False

    def delete(self, word):
        """Delete a word from the trie."""
        for i in range(len(word)):
            index = self.get_index(word[i])
            if not self.root:
                print(f'Word: {word} not found')
                return -1
            self.root = self.root.children.get(index)
        if not self.root:
            print(f'Word: {word} not found')
            return -1
        else:
            self.root.terminating = False
            return 0

    def update(self, old_word, new_word):
        """Update a word by removing one and replacing it with another."""
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)
```


```python
trie = Trie()

strings = ['word', 'words', 'wow', 'won', 'wont', 'tries', 'bow', 'cow']
for entry in strings:
    trie.insert(entry)

print(trie.search('wow'))
# trie.update('wow', 'well')
# trie.delete('well')
# print(trie.search('well'))
```

    Root:dict_keys([22, 19, 1, 2])
    <<<<dict_keys([14])
    <<<<dict_keys([17, 22, 13])
    <<<<dict_keys([])
    True



```python
trie.root.children.get(22).children
```




    defaultdict(None, {14: dict_keys([17, 22, 13])})




```python

```
