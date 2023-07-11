class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def search(curr, needle):
    if not curr:
        return False

    if curr.value == needle:
        return True

    if curr.value < needle:
        return search(curr.right, needle)

    return search(curr.left, needle)


def dfs(root, needle):
    return search(root, needle)


def main():
    a = Node(8)
    b = Node(3)
    c = Node(10)
    d = Node(1)
    e = Node(6)
    f = Node(14)
    g = Node(4)
    h = Node(7)
    i = Node(13)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    print(dfs(a, 4))
    print(dfs(a, 69))


if __name__ == "__main__":
    main()
