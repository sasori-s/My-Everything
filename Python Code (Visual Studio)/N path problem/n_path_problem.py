from collections import deque

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return str((self.x, self.y))
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def is_valid(x, y, N):
    return (0 <= x < N) and (0 <= y < N)

def get_path(node, path=[]):
    if node:
        get_path(node.parent, path)
        path.append(node)

def find_path(matrix, x=0, y=0):
    if not matrix or not len(matrix):
        return

    q = deque()
    N = len(matrix)
    src = Node(x, y)
    q.append(src)

    visited = set()
    key = (src.x, src.y)
    visited.add(key)

    while q:
        curr = q.popleft()
        i = curr.x
        j = curr.y

        if i == N - 1 and j == N - 1:
            path = []
            get_path(curr, path)
            return path

        n = matrix[i][j]

        for k in range(len(row)):
            x = i + row[k] * n
            y = j + col[k]

            if is_valid(x, y, N):
                next = Node(x, y, curr)
                key = (next.x, next.y)

                if key is not visited:
                    visited.add(key)
                    q.append(next)

    return


if __name__ == '__main__':
 
    matrix = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]
 
    # Find a route in the matrix from source cell (0, 0) to
    # destination cell (N-1, N-1)
    path = find_path(matrix)
 
    if path:
        print('The shortest path is', path)
    else:
        print('Destination is not found')



    
    