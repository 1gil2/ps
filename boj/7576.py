#silver 1

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

visit = [[0]*n for x in range(m)]
tomato = [list(map(int, sys.stdin.readline().split())) for x in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque()
ans = 0
zerocnt = 0
zerocnt2 = 0

for x in range(m):
    for y in range(n):
        if tomato[x][y] == 1:
            Q.append([x, y, 0])
            visit[x][y] = 1
        elif tomato[x][y] == -1:
            visit[x][y] = -1
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
        time = Q[0][2]
        Q.popleft()

        for d in range(4):
            dx1 = x1+dx[d]
            dy1 = y1+dy[d]

            if 0 <= dx1 < m and 0 <= dy1 < n and visit[dx1][dy1] == 0:
                visit[dx1][dy1] = 1
                Q.append([dx1, dy1, time+1])
                ans = max(ans, time+1)

    for x in range(m):
        for y in range(n):
            if visit[x][y] == 0:
                zerocnt2 += 1

    if zerocnt2 == 0:
        print(ans)
    else:
        print(-1)
