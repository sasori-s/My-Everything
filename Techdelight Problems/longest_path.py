import sys
from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dst, weight) in edges:
            self.adjList[src].append((dst, weight))
            self.adjList[dst].append((src, weight))

def find_max_cost(graph, src, k):
    q = deque()
    vertices = set([0])
    q.append((src, 0, vertices))
    maxcost = -sys.maxsize

    while q:
        v, cost, vertices = q.popleft()
        if cost > k:
            maxcost = max(maxcost, cost)

            for (dest, weight) in graph.adjList[v]:
                if not dest in vertices:
                    s = set(vertices)
                    s.add(dest)
                    q.append((dest, cost + weight, s))

    return maxcost


if __name__ == '__main__':
    # List of graph edges as per the above diagram
    edges = [
        (0, 6, 11), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, -8), (3, 4, 10),
        (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6)
    ]
    n = 8
    graph = Graph(edges, n)
    src = 0
    cost = 50

    max_cost = find_max_cost(graph, src, cost)
    if max_cost != -sys.maxsize:
        print(max_cost)
    else:
        print(f"All paths from source have their cost < {cost}")

