from os.path import curdir
from select import kevent
from tempfile import tempdir


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        new_node = Node(data=data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_after_key(self, node: Node, key: object):
        temp = self.head
        while temp:
            if temp.data == key:
                node.next = temp.next
                temp.next = node
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()

    # Insert some elements
    llist.insert_head(3)
    llist.insert_head(2)
    llist.insert_end(4)
    llist.insert_head(1)

    # Print the list
    llist.traversal()  # Output: 1 -> 2 -> 3 -> 4 -> None

    # Delete a node
    llist.delete_node(2)
    llist.traversal()  # Output: 1 -> 3 -> 4 -> None

