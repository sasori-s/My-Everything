from collections import deque
from typing import SupportsRound, Tuple
class Graph:
    def __init__(self, edges, N):
        self.adj_list = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adj_list[src].append(dest)

def findSolution(ladder, snake):
    N = 10 * 10
    edges = []
    for i in range(N):
        j = 1
        
        while j <= 6 and i + j <= N:
            src = i

            _ladder = ladder.get(i + j) if (ladder.get(i + j)) else 0
            _snake = snake.get(i + j) if (snake.get(i + j)) else 0

            if _ladder or _snake:
                dest = _ladder + _snake

            else:
                dest = i + j
            
            j = j + 1
            edges.append((src, dest))

    g = Graph(edges, N)
    BFS(g, 0, N)

def BFS(g, source, N):
    q = deque()
    discovered = [False] * (N + 1)   
    discovered[source] = True
    q.append((source, 0))

    while q:
        vertex, min_dist = q.popleft()

        if vertex == N:
            print(min_dist)
            break
        for u in g.adj_list[vertex]:
            if not discovered[u]:
                discovered[u] = True

                n = (u, min_dist + 1)
                q.append(n)



        


if __name__ == '__main__':
 
    # snakes and ladders are represented using a dictionary.
    ladder = {}
    snake = {}
 
    # insert ladders into the dictionary
    ladder[1] = 38
    ladder[4] = 14
    ladder[9] = 31
    ladder[21] = 42
    ladder[28] = 84
    ladder[51] = 67
    ladder[72] = 91
    ladder[80] = 99
 
    # insert snakes into the dictionary
    snake[17] = 7
    snake[54] = 34
    snake[62] = 19
    snake[64] = 60
    snake[87] = 36
    snake[93] = 73
    snake[95] = 75
    snake[98] = 79
 
    findSolution(ladder, snake)