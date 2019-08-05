# single link list


class Node():
    """The Node of a singly linked list, together with helper methods."""

    def __init__(self, node_value=None, next_node=None):
        """
        When linked list is first initialized, there are no nodes, so head is none.
        """
        self.node_value = node_value
        self.next = next_node  # pointer initially points to nothing

    def traverse(self):
        node = self
        while node is not None:
            node = node.next

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    """Singly Linked List with its operations."""

    def __init__(self, head: Node = None):
        """
        Initialize the head to either Node(if provided) or None(empty Linked list).
        """
        self.head = head

    def insert(self, data):
        new_node = Node(node_value=data)
        new_node.set_next(self.head)   # self.next = self.head
        self.head = new_node
        print(f'Head data value is now: {self.head.node_value}')

    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.get_next()
            count += 1
        return count

    def search(self, value):
        current = self.head
        found = False
        while current and found is False:
            if current.node_value == value:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError(f'Data: {value} not in linked list.')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.node_value == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            current = current.get_next()
        if current is None:
            raise ValueError('Data not in linked list.')
        else:
            previous.set_next(current.get_next())


if __name__ == '__main__':
    ll = LinkedList()

    data = range(10)
    for entry in data:
        ll.insert(entry)

    ll.search(7)
    ll.size()
    ll.delete(7)
    ll.search(7)
