# Implementation of a trie
from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, character):
        return ord(character) - ord('a')

    def insert(self, word):
        root = self.root
        for i in range(len(word)):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        root.terminating = True

    def search(self, word):
        root = self.root
        for i in range(len(word)):
            index = self.get_index(word[i])

            if not root:
                return False
            root = root.children.get(index)
        return True if root and root.terminating else False

    def delete(self, word):
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
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)


if __name__ == '__main__':
    trie = Trie()

    strings = ['word', 'words', 'wow', 'won']
    for entry in strings:
        trie.insert(entry)

    print(trie.search('wow'))
    trie.update('wow', 'well')
    print(trie.search('well'))
