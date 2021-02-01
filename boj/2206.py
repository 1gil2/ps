#gold 4

import sys
import math
from collections import deque
sys.setrecursionlimit(10 ** 6)
# input=sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    dq = deque()
    dq.append((0, 0, 0, 1))

    while dq:
        a = dq.popleft()
        x = a[0]
        y = a[1]
        broken = a[2]
        move = a[3]

        if x == n - 1 and y == m - 1:
            return move

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < n and 0 <= y1 < m:
                if table[x1][y1] == '1' and broken == 0:
                    visit[x1][y1][broken + 1] = 1
                    dq.append((x1, y1, 1, move + 1))
                elif table[x1][y1] == '0' and visit[x1][y1][broken] == 0:
                    visit[x1][y1][broken] = 1
                    dq.append((x1, y1, broken, move + 1))

    return -1


n, m = map(int, input().split())

table = [input() for x in range(n)]
visit = [[[0 for z in range(2)] for y in range(m)] for x in range(n)]
# [n][m][2] [x좌표][y좌표][벽 부쉈는지]
visit[0][0][0] = 1
print(bfs())
