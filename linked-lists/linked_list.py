# single link list


class Node():
    """The Node of a singly linked list, together with helper methods."""

    def __init__(self, value=None, next_node=None):
        """
        When linked list is first initialized, there are no nodes, so head is none.
        """
        self.value = value
        self.next = next_node  # pointer initially points to nothing

    def traverse(self):
        node = self
        while node is not None:
            node = node.next
            

class LinkedList():
    """Singly Linked List with its operations."""

    def __init__(self, head: Node = None):
        """
        Initialize the head to either Node(if provided) or None(empty Linked list).
        """
        self.head = head

    def insert(self, value):
        """O(1) time"""
        node = Node(value=value)
        node.next = self.head
        self.head = node

    def size(self):
        """O(n) time"""
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def search(self, value):
        """O(n) Worst case, it visits all the nodes."""
        current = self.head
        found = False
        while current and found is False:
            if current.value == value:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError(f'{value} not found.')
        return current

    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            current = current.next
        if current is None:
            raise ValueError('Data not in linked list.')
        else:
            # deletion happens here
            previous.next = current.next
            


if __name__ == '__main__':
    ll = LinkedList()

    data = range(10)
    for entry in data:
        ll.insert(entry)

    ll.search(7)
    ll.size()
    ll.delete(7)
    ll.search(7)
