#gold 1

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def atoi(alpha):
    if alpha.islower():
        return ord(alpha) - 71
    else:
        return ord(alpha) - 65


def up():
    up_dist[0][0] = 0
    heap = []
    heappush(heap, (0, 0, 0))

    while heap:
        di, x, y = heappop(heap)

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m:
                if table[x1][y1] - table[x][y] > t:
                    continue

                if table[x][y] >= table[x1][y1]:
                    cost = 1
                else:
                    cost = (table[x1][y1] - table[x][y]) ** 2

                if up_dist[x1][y1] > cost + di:
                    up_dist[x1][y1] = cost + di
                    heappush(heap, (cost + di, x1, y1))


def down():
    down_dist[0][0] = 0
    heap = []
    heappush(heap, (0, 0, 0))

    while heap:
        di, x, y = heappop(heap)

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m:
                if table[x1][y1] - table[x][y] > t:
                    continue

                if table[x][y] <= table[x1][y1]:
                    cost = 1
                else:
                    cost = (table[x1][y1] - table[x][y]) ** 2

                if down_dist[x1][y1] > cost + di:
                    down_dist[x1][y1] = cost + di
                    heappush(heap, (cost + di, x1, y1))


n, m, t, d = map(int, input().split())
table = []
for _ in range(n):
    tt = []
    temp = input().strip()
    for al in temp:
        tt.append(atoi(al))
    table.append(tt)

up_dist = [[sys.maxsize for y in range(m)] for x in range(n)]
down_dist = [[sys.maxsize for y in range(m)] for x in range(n)]

up()
down()

ans = 0
for x in range(n):
    for y in range(m):
        if up_dist[x][y] == sys.maxsize:
            continue
        if down_dist[x][y] == sys.maxsize:
            continue
        if up_dist[x][y] + down_dist[x][y] <= d:
            ans = max(ans, table[x][y])

print(ans)
