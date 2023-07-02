class QNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, node):
        if not self.tail:
            self.head = node
            self.tail = node

        self.tail.next = node
        self.tail = node

    def dequeu(self):
        if not self.head:
            return None

        h = self.head
        self.head = h.next
        h.next = None

        self.length -= 1
        return h.value

    def peek(self):
        if not self.head:
            return None

        return self.head.value


def main():
    q = Queue()
    n1 = QNode(value=1)
    n2 = QNode(value=2)
    n3 = QNode(value=3)
    n4 = QNode(value=4)

    q.enqueue(n1)
    q.enqueue(n2)
    q.enqueue(n3)
    q.enqueue(n4)

    curr = q.head
    while curr:
        print(curr.value)
        curr = curr.next



if __name__ == "__main__":
    main()
