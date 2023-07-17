class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    # def __hash__(self):
    #     return hash(self.value)
    #
    # def __eq__(self, other):
    #     return isinstance(other, Node) and self.value == other.value

    def __repr__(self):
        return f"{self.value}"


class LRU:
    def __init__(self, capacity=10):
        self.length = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.lookup = {}
        self.reverse_lookup = {}

    def update(self, key, value):
        node = self.lookup.get(key)
        if not node:
            node = Node(value)
            self.length += 1
            self.prepend(node)
            self.trim_cache()

            self.lookup[key] = node
            self.reverse_lookup[node] = key
        else:
            self.detach(node)
            self.prepend(node)
            node.value = value

    def get(self, key):
        node = self.lookup.get(key)
        if not node:
            return

        self.detach(node)
        self.prepend(node)

        return node.value

    def detach(self, node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if self.head == node:
            self.head = self.head.next

        if self.tail == node:
            self.tail = self.tail.prev

        node.next = None
        node.prev = None

    def prepend(self, node):
        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def trim_cache(self):
        if self.length <= self.capacity:
            return

        tail = self.tail
        self.detach(self.tail)

        key = self.reverse_lookup.get(tail)
        self.lookup.pop(key)
        self.length -= 1


def main():
    cache = LRU(5)
    cache.update("1", 1)
    cache.update("2", 2)
    cache.update("3", 3)
    cache.update("4", 4)
    x = cache.get("2")
    print(f"{x=}")
    cache.update("5", 5)
    y = cache.get("1")
    print(f"{y=}")
    print(cache.length)
    cache.update("6", 6)
    cache.update("7", 7)
    print(cache.length)

    print("*" * 5)
    curr = cache.head
    while curr:
        print(curr)
        curr = curr.next


if __name__ == "__main__":
    main()
