class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return

        prev = None
        cur = self.head

        while True:
            if cur.data == key:

                if cur.next == self.head and cur == self.head:
                    self.head = None

                elif cur == self.head:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    self.head = cur.next
                    tail.next = self.head

                else:
                    prev.next = cur.next

                return

            prev = cur
            cur = cur.next

            if cur == self.head:
                break

    def iterate(self):
        if not self.head:
            return

        cur = self.head

        while True:
            print(cur.data)
            cur = cur.next

            if cur == self.head:
                break


cll = CircularLinkedList()

cll.append(10)
cll.append(20)
cll.append(30)

cll.iterate()


