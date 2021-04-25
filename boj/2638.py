#gold 4

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    dq = deque()
    dq.append((0, 0))
    table[0][0] = 2

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m and table[x1][y1] == 0:
                table[x1][y1] = 2
                dq.append((x1, y1))


n, m = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]

time = 0
while True:
    total = 0
    for t in table:
        total += sum(t)

    if total == 0:
        break

    # 외부 2으로 변환
    bfs()

    # 2로 둘러싸인 곳 2로 변환
    for x in range(n):
        for y in range(m):
            if table[x][y] != 1:
                continue
            cnt = 0
            for i in range(4):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < n and 0 <= y1 < m and table[x1][y1] == 2:
                    cnt += 1
            if cnt >= 2:
                table[x][y] = 3

    # 2를 전부 0으로 변환
    for x in range(n):
        for y in range(m):
            if table[x][y] == 2 or table[x][y] == 3:
                table[x][y] = 0
    time += 1

print(time)
