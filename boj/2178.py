#silver 1

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
table = [input() for x in range(n)]
visit = [[0 for y in range(m)] for x in range(n)]

visit[0][0] = 1
q = [[0, 0]]
dq = deque(q)

while dq:
    x, y = dq.popleft()
    temp = visit[x][y]

    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]

        if 0 <= y1 < m and 0 <= x1 < n and visit[x1][y1] == 0 and table[x1][y1] == '1':
            dq.append([x1, y1])
            visit[x1][y1] = temp+1

print(visit[-1][-1])
