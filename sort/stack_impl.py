class SNode:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class Stack:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def push(self, node):
        h = self.head
        if not h:
            self.head = node
            self.length += 1
            return

        self.head = node
        self.head.prev = h
        self.length += 1

    def pop(self):
        h = self.head
        if not h:
            return None

        self.head = h.prev
        h.prev = None
        self.length = max(0, self.length - 1)

        return h.value

    def peek(self):
        if not self.head:
            return None

        return self.head.value


def main():
    s = Stack()
    n1 = SNode(value=1)
    n2 = SNode(value=2)
    n3 = SNode(value=3)
    n4 = SNode(value=4)

    s.push(n1)
    s.push(n2)
    s.push(n3)
    s.push(n4)

    while s.length:
        print(s.pop())


if __name__ == "__main__":
    main()
