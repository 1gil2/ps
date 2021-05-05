#silver 2

import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    dq = deque()
    dq.append((0, sx, sy))
    visit = [[0 for x in range(n+1)] for y in range(n+1)]
    visit[sx][sy] = 1

    while dq:
        cnt, x, y = dq.popleft()

        if x == ex and y == ey:
            print(cnt)
            break

        for i in range(8):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < n and visit[x1][y1] == 0:
                visit[x1][y1] = 1
                dq.append((cnt+1, x1, y1))
