from collections import deque
class Graph:
    def __init__(self, edges, n):
        self.adjlist = [[] for _ in range(n)]

        for (src, dst) in edges:
            self.adjlist[src].append(dst)
            self.adjlist[dst].append(src)


def BFS(graph, src, n):
    discovered = [False] * n
    discovered[src] = True
    q = deque()
    q.append((src, -1))

    while q:
        (v, parent) = q.popleft()

        for u in graph.adjlist[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append((u, v))

            elif u != parent:
                return True
    
    return False

if __name__ == "__main__":
    edges = [
        (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (4, 8),
        (4, 9), (3, 6), (3, 7), (6, 10), (6, 11), (5, 9)]

    n = 12
    graph = Graph(edges, n)

    if BFS(graph, 0, n):
        print("This graph contains a cycle")

    else:
        print("The graph doesn\'t contain any cycle")
       