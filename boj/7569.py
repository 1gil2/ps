#silver 1
#pypy3

import sys
from collections import deque

n, m, h = map(int, input().split())

visit = [[[0] * n for x in range(m)] for y in range(h)]
tomato = [[list(map(int, input().split())) for x in range(m)] for y in range(h)]
# tomato[h][m][n], visit[h][m][n]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

Q = deque()
ans = 0
zerocnt = 0
zerocnt2 = 0

for x in range(m):
    for y in range(n):
        for z in range(h):
            if tomato[z][x][y] == 1:
                Q.append([x, y, z, 0])
                visit[z][x][y] = 1
            elif tomato[z][x][y] == -1:
                visit[z][x][y] = -1
            else:
                zerocnt += 1

if zerocnt == 0:
    print(0)
else:
    while True:
        if len(Q) == 0:
            break
        x1 = Q[0][0]
        y1 = Q[0][1]
        z1 = Q[0][2]
        time = Q[0][3]
        Q.popleft()

        for d in range(6):
            dx1 = x1 + dx[d]
            dy1 = y1 + dy[d]
            dz1 = z1 + dz[d]

            if 0 <= dx1 < m and 0 <= dy1 < n and 0 <= dz1 < h and visit[dz1][dx1][dy1] == 0:
                visit[dz1][dx1][dy1] = 1
                Q.append([dx1, dy1, dz1, time + 1])
                ans = max(ans, time + 1)

    for x in range(m):
        for y in range(n):
            for z in range(h):
                if visit[z][x][y] == 0:
                    zerocnt2 += 1

    if zerocnt2 == 0:
        print(ans)
    else:
        print(-1)
