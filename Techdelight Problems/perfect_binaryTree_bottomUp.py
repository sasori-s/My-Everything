from collections import deque

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def printNodes(root):
    if root is None:
        return

    level = 1
    d = {}
    d.setdefault(level, []).append(root.key)
    q1 = deque()
    q2 = deque()

    if root.left and root.right:
        q1.append(root.left)
        q2.append(root.right)

    while q1:
        level = level + 1
        n = len(q1)

        while n > 0:
            x = q1.popleft()
            d.setdefault(level, []).append(x.key)

            if x.left:
                q1.append(x.left)

            if x.right:
                q1.append(x.right)

            y = q2.popleft()
            d.setdefault(level, []).append(y.key)

            if y.left:
                q2.append(y.left)

            if y.right:
                q2.append(y.right)

            n = n - 1

    for i in reversed(d.keys()):
        print(d.get(i), end='')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    printNodes(root)



