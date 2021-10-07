#silver 2

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    dq = deque()
    dq.append((a, b))
    visit[a][b] = 1
    s = 0
    w = 0

    if table[a][b] == 'o':
        s += 1
    elif table[a][b] == 'v':
        w += 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < r and 0 <= y1 < c and table[x1][y1] != '#' and visit[x1][y1] == 0:
                visit[x1][y1] = 1

                if table[x1][y1] == 'o':
                    s += 1
                elif table[x1][y1] == 'v':
                    w += 1

                dq.append((x1, y1))

    return s, w


r, c = map(int, input().split())
table = [input().rstrip() for x in range(r)]
visit = [[0 for y in range(c)] for x in range(r)]

sheep = 0
wolf = 0

for x in range(r):
    for y in range(c):
        if table[x][y] != '#' and visit[x][y] == 0:
            s = 0
            w = 0

            s1, w1 = bfs(x, y)

            s += s1
            w += w1

            if s > w:
                w = 0
            else:
                s = 0

            sheep += s
            wolf += w

print(sheep, wolf)
