class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    path = []
    q = [root]
    while q:
        curr = q.pop(0)
        path.append(curr.value)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    return path


# depth first search preserve shape while breath first search does not
def compare(a, b):
    if not a and not b:
        return True

    if not a or not b:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


def main():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    z = Node("z")
    y = Node("y")
    x = Node("x")

    a.left = b
    a.right = c
    b.left = d
    c.left = e

    z.left = y
    y.left = x

    print(bfs(a))
    print(compare(a, z))
    print(compare(a, a))
    print(compare(z, z))


if __name__ == "__main__":
    main()
