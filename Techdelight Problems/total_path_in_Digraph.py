from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)

def findTotalPaths(graph, src, dest, m):
    q = deque()
    q.append((src, 0))
    count = 0

    while q:
        vertex, deapth = q.popleft()

        if vertex == dest and deapth == m:
            count = count + 1

        if deapth > m:
            break

        for u in graph.adjList[vertex]:
            q.append((u, deapth + 1))

    return count

if __name__ == '__main__':
    edges = [
        (0, 6), (0, 1), (1, 6), (1, 5), (1, 2), (2, 3), (3, 4),
        (5, 2), (5, 3), (5, 4), (6, 5), (7, 6), (7, 1)
    ]
    n = 8
    graph = Graph(edges, n)
    src, dest = 0, 3
    m = 4

    print(findTotalPaths(graph, src, dest, m))



