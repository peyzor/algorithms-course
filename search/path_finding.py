dir = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x} y: {self.y}"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


def walk(maze, wall, curr, end, seen, path):
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False

    if maze[curr.y][curr.x] == wall:
        return False

    if curr.x == end.x and curr.y == end.y:
        path.append(curr)
        return True

    if seen[curr.y][curr.x]:
        return False

    seen[curr.y][curr.x] = True
    path.append(curr)

    for i in range(len(dir)):
        x, y = dir[i]
        current = Point(x=curr.x + x, y=curr.y + y)
        if walk(maze, wall, current, end, seen, path):
            return True

    path.pop()
    return False


def solve(maze, wall, start, end):
    seen = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []

    walk(maze, wall, start, end, seen, path)
    return path


def main():
    maze = [
        "#####E#",
        "#     #",
        "#S#####",
    ]
    goodmaze = [
        "x     E xx",
        "xxx xxxxxx",
        "x x xxxxxx",
        "x       xx",
        "xx x x    ",
        "xxx x xxxS",
    ]

    def find_char(maze, char):
        for y in range(len(maze)):
            try:
                x = maze[y].index(char)
            except ValueError:
                continue

            if x:
                return x, y

    print(find_char(goodmaze, "S"))
    print(find_char(goodmaze, "E"))

    # result = solve(maze, "#", Point(x=1, y=2), Point(x=5, y=0))
    # print(result)
    res = solve(goodmaze, "x", Point(x=9, y=5), Point(x=6, y=0))
    print(res)


if __name__ == "__main__":
    main()
