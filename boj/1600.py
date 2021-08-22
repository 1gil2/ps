#gold 4

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs():
    visit = [[[0 for z in range(k + 1)] for y in range(w)] for x in range(h)]
    dq = deque()
    dq.append((0, 0, k))

    while dq:
        x, y, horse = dq.popleft()

        if x == h - 1 and y == w - 1:
            print(visit[x][y][horse])
            return

        if horse:
            for i in range(8):
                x1 = x + hx[i]
                y1 = y + hy[i]

                if 0 <= x1 < h and 0 <= y1 < w and table[x1][y1] == 0 and visit[x1][y1][horse - 1] == 0:
                    visit[x1][y1][horse - 1] = visit[x][y][horse] + 1
                    dq.append((x1, y1, horse - 1))

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < h and 0 <= y1 < w and table[x1][y1] == 0 and visit[x1][y1][horse] == 0:
                visit[x1][y1][horse] = visit[x][y][horse] + 1
                dq.append((x1, y1, horse))
    print(-1)
    return


k = int(input())
w, h = map(int, input().split())

table = [list(map(int, input().split())) for x in range(h)]
bfs()
