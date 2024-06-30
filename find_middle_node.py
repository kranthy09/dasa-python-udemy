"""
Linked List method to return a middle node
"""


class LinkedList:
    """Linked List implementation"""

    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1 if data is not None else 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def find_middle_node(self):
        pass
