#gold 4

import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def check(x, y, i, k):
    for a in range(1, k + 1):
        if table[x + dx[i] * a][y + dy[i] * a] == 1:
            return False
    return True


def turn(vec, flag):
    if vec == 1:
        if flag:
            return 4
        return 3
    if vec == 2:
        if flag:
            return 3
        return 4
    if vec == 3:
        if flag:
            return 2
        return 1
    if vec == 4:
        if flag:
            return 1
        return 2


def bfs():
    visit = [[[0 for v in range(5)] for y in range(n)] for x in range(m)]
    heap = []
    heappush(heap, [0, sx - 1, sy - 1, sv])

    while heap:
        cnt, x, y, v = heappop(heap)

        if x == ex - 1 and y == ey - 1 and v == ev:
            print(cnt)
            return

        left = turn(v, True)
        right = turn(v, False)
        if visit[x][y][left] == 0:
            visit[x][y][left] = 1
            heappush(heap, [cnt + 1, x, y, left])
        if visit[x][y][right] == 0:
            visit[x][y][right] = 1
            heappush(heap, [cnt + 1, x, y, right])

        for k in range(1, 4):
            x1 = x + dx[v - 1] * k
            y1 = y + dy[v - 1] * k

            if 0 > x1 or 0 > y1 or m <= x1 or n <= y1:
                continue

            if visit[x1][y1][v] == 0 and check(x, y, v - 1, k):
                visit[x1][y1][v] = 1
                heappush(heap, [cnt + 1, x1, y1, v])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
table = [list(map(int, input().split())) for x in range(m)]

sx, sy, sv = map(int, input().split())
ex, ey, ev = map(int, input().split())

bfs()
