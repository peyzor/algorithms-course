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


def main():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    a.left = b
    a.right = c
    b.left = d
    c.left = e

    print(bfs(a))


if __name__ == "__main__":
    main()
