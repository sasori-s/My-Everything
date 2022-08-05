import sys
from collections import deque

row = [-1, 0, 0, 1]
col = [0, 1, -1, 0]

def isSafe(field, visited, x, y):
    return field[x][y] == 1 and not visited[x][y]

def isValid(x, y, M, N):
    return M > x >= 0 and N > y >= 0

def BFS(field):
    (M, N) = (len(field), len(field[0]))
    q = deque()
    visited = [[False for x in range(N)] for y in range(M)]

    for r in range(M):
        if field[r][0] == 1:
            q.append((r, 0, 0))
            visited[r][0] = True
    
    while q:
        (i, j, dist) = q.popleft()

        if j == N - 1:
            return dist

        for k in range(len(row)):
            if isValid(i + row[k], j + col[k], M, N) and isSafe(field, visited, i + row[k], j+ col[k]):
                q.append((i + row[k], j + col[k], dist + 1))

    return sys.maxsize

def findShortestDistance(mat):
    if not mat or not len(mat):
        return 0

    (M, N) = (len(mat), len(mat[0]))
    r = [-1, -1, -1, 0, 0, 1, 1, 1]
    c = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(M):
        for j in range(N):
            for k in range(len(r)):
                if mat[i][j] == 0 and isValid(i + c[k], j + c[k], M, N) \
                    and mat[i + r[k]][j + c[k]] == 1:
                    mat[i + r[k]][j + c[k]] = sys.maxsize

    for i in range(M):
        for j in range(N):
            if mat[i][j] == sys.maxsize:
                mat[i][j] = 0

    return BFS(mat)

if __name__ == "__main__":
    
    field = [
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    M = N = len(field)
    dist = findShortestDistance(field)

    if dist != sys.maxsize:
        print("The shortest path has a length of ", dist)
    else:
        print("There is no shortest path")

    for i in range(M):
        for j in range(N):
            print(field[i][j], end=" ")
        print()