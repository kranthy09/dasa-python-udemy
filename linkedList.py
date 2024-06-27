class Node:
    """Represents value and next for a Node"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Nodes Linked as a List"""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


mylinked_list = LinkedList(4)
print(mylinked_list.head.value)
