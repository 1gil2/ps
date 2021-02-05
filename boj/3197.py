#gold 1
#pypy 3

from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while q:
        x, y = q.popleft()

        if x == x2 and y == y2:
            return 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny]:
                    if table[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    visit[nx][ny] = 1
    return 0


def melt():
    while waterq:
        x, y = waterq.popleft()

        if table[x][y] == 'X':
            table[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not water_visit[nx][ny]:
                    if table[nx][ny] == 'X':
                        waterq_temp.append([nx, ny])

                    water_visit[nx][ny] = 1


m, n = map(int, sys.stdin.readline().split())
visit = [[0] * n for x in range(m)]
water_visit = [[0] * n for x in range(m)]

table = []
swan = []
q, q_temp, waterq, waterq_temp = deque(), deque(), deque(), deque()

for x in range(m):
    L = list(sys.stdin.readline().strip())
    table.append(L)
    for y in range(len(L)):
        if table[x][y] == 'L':
            swan.extend([x, y])
            waterq.append([x, y])
        elif table[x][y] == '.':
            water_visit[x][y] = 1
            waterq.append([x, y])

x1, y1, x2, y2 = swan
q.append([x1, y1])
table[x1][y1], table[x2][y2], visit[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, waterq = q_temp, waterq_temp
    q_temp, waterq_temp = deque(), deque()
    cnt += 1
