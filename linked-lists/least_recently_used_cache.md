## Problem
Implement a class to define an LRU(Least Recently Used) Cache. The class should allow for insertion of key-value pairs, retrieve a value using a key, and getting the most recent key.
When a key/value is inserted, the key should become the most recently used key.

- The LRUCache should store a maximum capacity (max_size) which indicates the maximum key/value pairs the cache can hold at once. It will is also be passed when the class is instantiated.

- If a key/value pair is added to the cache when the maximum capacity is reached, the cache should evict the least recently used key/value pair.

- If inserting a key/value pair that already exists in the cache, the cache should only update the value and not remove the key/value pair.

- If you attempt to retrieve a value of a key that's not in the cache should return a null value.



```python
class LRUCache:
    def __init__(self, max_size):
        self.cache = {}
        self.current_size = 0
        self.max_size = max_size or 1
        self.doubly_linked_list = DoublyLinkedList()
    
    def evict_least_recent(self):
        key_to_remove = self.doubly_linked_list.tail.key
        # remove tail from doubly linked list
        self.doubly_linked_list.remove_tail()
        # remove key from hash table pointing to the former tail we just removed
        del self.cache[key_to_remove]
        
    def get(self, key):
        """O(1) time | O(1) space."""
        
        node = self.cache.get(key, None)
        if not node:
            return None
        self.update_most_recent(node)
        return node.value
    
    def get_most_recent_key(self):
        """O(1) time | O(1) space."""
        return self.doubly_linked_list.head.key
    
    def insert(self, key, value):
        """O(1) time | O(1) space."""
        
        if key not in self.cache:
            # If no capacity, evict tail
            if self.current_size == self.max_size:
                self.evict_least_recent()
            else:
                self.current_size += 1
            # Put new key in cache to point to new node
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            # Update already existing node
            self.update_key(key, value)
        # Update the doubly linked list
        self.update_most_recent(self.cache[key])

    def update_key(self, key, value):
        # update existing key with new value
        if key not in self.cache:
            raise Exception("The provided key is not in the cache!")
        self.cache[key].value = value
    
    def update_most_recent(self, node):
        self.doubly_linked_list.set_head(node)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.previous = node
            node.next = self.head
            self.head = node
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            self.head.previous = node
            node.next = self.head
            self.head = node
            
    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        
        # Update new tail to be previous node, & set tail to point to Null value.
        self.tail = self.tail.previous
        self.tail.next = None
        
    
class DoublyLinkListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def remove_bindings(self):
        if self.previous is not None:
            self.previous.next = self.next
        if self.next is not None:
            self.next.previous = self.previous
        self.previous = None
        self.next = None
```


```python

```
