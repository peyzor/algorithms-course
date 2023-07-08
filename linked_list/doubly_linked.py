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

    def debug(self):
        out = ""
        i = 0
        curr = self.head
        while curr:
            out += f"{curr.prev.value if curr.prev else None} -> {curr.value} "
            out += f"{curr.value} -> {curr.next.value if curr.next else None} "
            curr = curr.next
            i += 1

        return out


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

    def remove(self, value):
        i = 0
        curr = self.head
        while curr and i < self.length:
            if curr.value == value:
                if curr.prev:
                    curr.prev.next = curr.next

                if curr.next:
                    curr.next.prev = curr.prev

                if curr == self.head:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = curr.prev

                curr.prev = None
                curr.next = None
                self.length -= 1
                return curr.value

            curr = curr.next

    def get(self, idx):
        i = 0
        curr = self.head
        while curr:
            if i == idx:
                return curr

            curr = curr.next
            i += 1

    def remove_at(self, idx):
        i = 0
        curr = self.head
        while curr:
            if i == idx:
                if curr.prev:
                    curr.prev.next = curr.next

                if curr.next:
                    curr.next.prev = curr.prev

                if curr == self.head:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = curr.prev

                curr.prev = None
                curr.next = None
                self.length -= 1
                return curr.value

            curr = curr.next
            i += 1


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
    dll.remove("B")
    dll.remove_at(0)
    print("length after removals", dll.length)

    curr = dll.head
    while curr:
        print(curr.value)
        curr = curr.next

    print()
    rcurr = dll.tail
    while rcurr:
        print(rcurr.value)
        rcurr = rcurr.prev

    print()
    print(dll.debug())


if __name__ == "__main__":
    main()
