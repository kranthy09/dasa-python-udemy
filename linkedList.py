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

    def print_list(self):
        """prints elements in the linked list"""

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, item):
        """Appends new item to the linked list"""
        new_node = Node(item)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        """removes last element from the LinkedList"""
        if self.length == 0:
            return "can't pop empty list"
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        """add element in the start"""

        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self):
        """pops first element from the LinkedList"""

        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next

        self.length -= 1
        return temp

    def get(self, index):
        """returns the value at an index"""
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value

    def set_value(self, index, value):
        """set the value at an index"""
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value

        return True


mylinked_list = LinkedList(4)
mylinked_list.append(2)
mylinked_list.append(6)
mylinked_list.append(7)
print(mylinked_list.head.value)
mylinked_list.print_list()
print(mylinked_list.pop())
print("\nAfter popping last element:")
mylinked_list.print_list()

print(mylinked_list.pop())
print("\nAfter popping last element:")
mylinked_list.print_list()
mylinked_list.append(11)
print("\nAfter appending 11:")
mylinked_list.print_list()
mylinked_list.prepend(21)
print("\nAfter prepending 21:")
mylinked_list.print_list()
mylinked_list.pop_first()
print("\nAfter popping first element:")
mylinked_list.print_list()

print("\n get the value at an index")

print(mylinked_list.get(2))
print(mylinked_list.get(5))


mylinked_list.set_value(2, 33)
print("\nAfter setting value at index 2 to 33:")
mylinked_list.print_list()
