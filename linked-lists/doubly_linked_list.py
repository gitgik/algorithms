class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None

    def set_head(self, node):
        """
        Set the head of the linked list.
        Complexity:
            O(1) time | O(1) space
        """
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    def set_tail(self, node):
        """
        Set the tail of the linked list.
        Complexity:
            O(1) time | O(1) space
        """
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail, node)

    def insert_before(self, node, node_to_insert):
        """
        Insert a node before the specified node.
        Complexity:
            O(1) time | O(1) space
        """
        if node_to_insert == self.head and node_to_insert == node.tail:
            # node already exists as tail or head
            return
        # first, remove the node to insert currently exists in the linked list
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node

        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    def insert_after(self, node, node_to_insert):
        """
        Insert a new node after the specified node.
        Complexity:
            O(1) time | O(1) space
        """
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        # first remove the node to insert if it currently exists in the linked list
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.next = node_to_insert

    def insert_at_position(self, position, node_to_insert):
        """
        Insert a node at a position
        Complexity:
            O(p) time  - since we are iterating up until position p
            O(1) space - constant time setting of pointers
        """
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1
        if node is not None:
            self.insert_before(node, node_to_insert)
        else:
            # node is None so we are at the tail
            self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value):
        """
        Remove a node that contains this value.
        Complexity:
            O(n) time  where n is the size of the linked list
            O(1) space
        """
        node = self.head
        while node is not None:
            # temporary save the current node, to not lose it while we check
            # if it needs to be removed
            node_to_remove = node
            # update the node to be the next node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove(self, node):
        """
        Remove a node from the list
        Complexity:
            O(1) time | O(1) space
        """
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.update_node_bindings(node)

    def contains_node_with_value(self, value):
        """
        Return True if the linked list contains a node with the input value.
        Complexity:
            O(n) time | O(1) space
        """
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def update_node_bindings(self, node):
        """
        Update the pointers of a node when a node is removed from the doubly linked list.
        """
        # the order in which you remove pointers matters. otherwise, we might delete nodes
        # and never recover them forever.

        if node.prev is not None:
            node.prev.next = node.next
        node.prev = None
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None


if __name__ == '__main__':
    doubly_linked_list = DoubleLinkedList()
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    doubly_linked_list.set_head(first_node)
    doubly_linked_list.set_tail(third_node)
    doubly_linked_list.insert_before(third_node, second_node)
    another_node = Node(7)
    doubly_linked_list.insert_after(third_node, another_node)
