from collections import deque


def isValid(i, j, N, M):
    return (0 <= i < M) and (0 <= j < N)

def isSafe(i, j, mat, result):
    return mat[i][j] == 'O' and result[i][j] == -1

def updateShortestDistance(mat):
    if not mat or not len(mat):
        return []
    
    (M, N) = (len(mat), len(mat[0]))
    result = [[0 for i in range(N)] for j in range(M)]
    q = deque()

    for i in range(M):
        for j in range(N):
            if mat[i][j] == "M":
                q.append((i, j, 0))
                result[i][j] = 0
            
            else:
                result[i][j] = -1

    row = [0, -1, 0, 1]
    col = [1, 0, -1, 0]

    while q:
        x, y, distance = q.popleft()

        for i in range(len(row)):
            if isValid(x + row[i], y + col[i], N, M) and \
                isSafe(x + row[i], y + col[i], mat, result):
                result[x + row[i]][y + col[i]] = distance + 1
                q.append((x + row[i], y + col[i], distance + 1))

    return result



if __name__ == '__main__':
 
    mat = [
        ['O', 'M', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'O', 'M'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'O', 'M', 'O', 'O'],
        ['O', 'X', 'X', 'M', 'O']
    ]
 
    result = updateShortestDistance(mat)
 
    # print results
    for r in result:
        print(r)