class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def prepend(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1

    def append(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            self.length += 1
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1

    def insert_at(self, node, idx):
        if idx > self.length:
            raise ValueError(f"index: {idx} bigger than length: {self.length}")

        elif idx == self.length:
            self.append(node)
            return

        elif idx == 0:
            self.prepend(node)
            return

        i = 0
        curr = self.head
        while curr and i <= idx:
            if i == idx:
                node.next = curr
                node.prev = curr.prev
                if curr.prev:
                    curr.prev.next = node

                curr.prev = node

                self.length += 1
                return

            curr = curr.next
            i += 1

        return


def main():
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")

    dll = DoublyLinkedList()
    dll.append(node_a)
    dll.append(node_b)
    dll.append(node_c)
    dll.append(node_d)
    print("length", dll.length)
    dll.insert_at(node_e, 2)
    print("length after insert", dll.length)

    curr = dll.head
    while curr:
        print(curr.value)
        curr = curr.next


if __name__ == "__main__":
    main()
