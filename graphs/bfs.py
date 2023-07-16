def bfs(graph, source, needle):
    seen = [False for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]

    seen[source] = True
    q = [source]
    while q:
        curr = q.pop(0)
        if curr == needle:
            break

        seen[curr] = True
        adjs = graph[curr]
        for i in range(len(adjs)):
            if adjs[i] == 0:
                continue

            if seen[i]:
                continue

            seen[i] = True
            prev[i] = curr
            q.append(i)

    curr = needle
    out = []
    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]

    if not out:
        return []

    out.reverse()
    return [source, *out]


def main():
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0]
    ]

    source = 1
    needle = 5

    out = bfs(graph, source, needle)
    print(out)


if __name__ == "__main__":
    main()
