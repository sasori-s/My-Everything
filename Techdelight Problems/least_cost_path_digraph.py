import sys
from collections import deque

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))

def findLeastCost(g, src, dest, m):
    q = deque()
    q.append((src, 0, 0))
    min_cost = sys.maxsize

    while q:
        v, deapth, cost = q.popleft()

        if v == dest and deapth == m:
            min_cost = min(min_cost, cost)

        if deapth > m:
            break

        for (des, weight) in g.adjList[v]:
            q.append((des, deapth + 1, cost + weight))

    return min_cost

if __name__ == '__main__':
    edges = [
        (0, 6, -1), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, 8), (3, 4, 10),
        (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6)
    ]
    n = 8
    g = Graph(edges, n)
    (src, dest) = (0, 3)
    m = 4
    print(findLeastCost(g, src, dest, m))