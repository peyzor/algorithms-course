class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

    def __repr__(self):
        return f"{self.to=} - {self.weight=}"


def has_unvisited(seen, dists):
    for s, d in zip(seen, dists):
        if not s and d < float('inf'):
            return True

    return False


def get_lowest_unvisited(seen, dists):
    idx = -1
    lowest_dst = float('inf')

    for i in range(len(seen)):
        if seen[i]:
            continue

        if dists[i] < lowest_dst:
            lowest_dst = dists[i]
            idx = i

    return idx


def djikstra_list(graph, source, needle):
    seen = [False for _ in range(len(graph))]
    dists = [float('inf') for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]

    dists[source] = 0

    while has_unvisited(seen, dists):
        curr = get_lowest_unvisited(seen, dists)
        seen[curr] = True

        adjs = graph[curr]
        for i in range(len(adjs)):
            edge = adjs[i]
            if seen[edge.to]:
                continue

            dist = dists[curr] + edge.weight
            if dist < dists[edge.to]:
                dists[edge.to] = dist
                prev[edge.to] = curr

    out = []
    curr = needle
    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]

    if not out:
        return []

    out.reverse()
    return [source, *out]


def main():
    graph = {
        0: [Edge(1, 1), Edge(3, 1)],
        1: [Edge(2, 5)],
        2: [],
        3: [Edge(4, 2)],
        4: [Edge(1, 1), Edge(2, 3)],
    }
    out = djikstra_list(graph, 0, 2)
    print(out)


if __name__ == "__main__":
    main()
