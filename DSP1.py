class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_first_node(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        prev = None
        current = self.head

        while current.next:
            prev = current
            current = current.next

        prev.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Original List:")
ll.display()

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:")
ll.display()

ll.insert_at_end(5)
print("After inserting 5 at end:")
ll.display()

ll.insert_at_position(15, 2)
print("After inserting 15 at position 2:")
ll.display()

ll.delete_first_node()
print("After deleting first node:")
ll.display()

ll.delete_last_node()
print("After deleting last node:")
ll.display()

ll.delete_at_position(1)
print("After deleting node at position 1:")
ll.display()