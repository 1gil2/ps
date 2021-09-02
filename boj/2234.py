#gold 4

import sys
from collections import deque

input = sys.stdin.readline

dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visit[x][y] = True
    room = 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            if table[x][y] & (1 << i) == 0:
                x1 = x + dx[i]
                y1 = y + dy[i]

                if 0 <= x1 < m and 0 <= y1 < n:
                    if not visit[x1][y1]:
                        visit[x1][y1] = True
                        dq.append((x1, y1))
                        room += 1

    return room


n, m = map(int, input().split())
table = [list(map(int, input().split())) for x in range(m)]
visit = [[False for y in range(n)] for x in range(m)]

cnt = 0
size = 0
size2 = 0

for x in range(m):
    for y in range(n):
        if not visit[x][y]:
            cnt += 1
            size = max(size, bfs(x, y))

for x in range(m):
    for y in range(n):
        for i in range(4):
            if table[x][y] & (1 << i):
                visit = [[False for y in range(n)] for x in range(m)]
                table[x][y] ^= (1 << i)
                size2 = max(size2, bfs(x, y))
                table[x][y] ^= (1 << i)

print(cnt)
print(size)
print(size2)
