from collections import deque
class Graph:
    def __init__(self, edges=None, n=0):
        self.n = n
        self.adjList = [[]for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isBipartite(graph):
    v = 0
    discovered = [False] * graph.n
    level = [None] * graph.n
    discovered[v] = True
    level[v] = 0

    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                level[u] = level[v] + 1
                q.append(u)

            elif level[v] == level[u]:
                return False

    return True

if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]

    n = 9
    graph = Graph(edges, n)

    if isBipartite(graph):
        print("Graph is Bipartite")
    else:
        print("graph is not Bipartite")
