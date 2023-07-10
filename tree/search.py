class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def walk(curr, path):
    if not curr:
        return path


    # preorder
    path.append(curr.value)
    walk(curr.left, path)
    # inorder
    # path.append(curr.value)
    walk(curr.right, path)
    # postorder 
    # path.append(curr.value)

    return path


def serach(root):
    return walk(root, [])


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

    path = serach(a)
    print(path)


if __name__ == "__main__":
    main()
