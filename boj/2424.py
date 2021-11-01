#platinum 3

import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
inf = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def pirate_map():
    dq = deque()
    dq.append((px, py))
    pirate[px][py] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m and table[x1][y1] == '.':
                if pirate[x1][y1] > pirate[x][y] + 1:
                    pirate[x1][y1] = pirate[x][y] + 1
                    dq.append((x1, y1))


def danger_map():
    danger1 = deepcopy(pirate)
    danger2 = deepcopy(pirate)
    danger3 = deepcopy(pirate)
    danger4 = deepcopy(pirate)

    for x in range(n):
        temp = inf
        for y in range(m):
            if table[x][y] == 'I':
                temp = inf
                danger1[x][y] = inf
                continue
            temp = min(temp, pirate[x][y])
            danger1[x][y] = temp

    for x in range(n):
        temp = inf
        for y in range(m - 1, -1, -1):
            if table[x][y] == 'I':
                temp = inf
                danger2[x][y] = inf
                continue
            temp = min(temp, pirate[x][y])
            danger2[x][y] = temp

    for y in range(m):
        temp = inf
        for x in range(n):
            if table[x][y] == 'I':
                temp = inf
                danger3[x][y] = inf
                continue
            temp = min(temp, pirate[x][y])
            danger3[x][y] = temp

    for y in range(m):
        temp = inf
        for x in range(n - 1, -1, -1):
            if table[x][y] == 'I':
                temp = inf
                danger4[x][y] = inf
                continue
            temp = min(temp, pirate[x][y])
            danger4[x][y] = temp

    for x in range(n):
        for y in range(m):
            danger[x][y] = min(danger1[x][y], danger2[x][y], danger3[x][y], danger4[x][y])


def bfs():
    dq = deque()
    dq.append((0, sx, sy))
    visit = [[False for y in range(m)] for x in range(n)]
    visit[sx][sy] = True

    while dq:
        cnt, x, y = dq.popleft()

        if x == ex and y == ey:
            print('YES')
            return

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m and table[x1][y1] == '.' and visit[x1][y1] == False:
                if danger[x1][y1] > cnt + 1:
                    visit[x1][y1] = True
                    dq.append((cnt + 1, x1, y1))

    print('NO')
    return


n, m = map(int, input().split())
table = [list(input().rstrip()) for x in range(n)]
pirate = [[inf for y in range(m)] for x in range(n)]
danger = [[inf for y in range(m)] for x in range(n)]
for x in range(n):
    for y in range(m):
        if table[x][y] == 'V':
            table[x][y] = '.'
            px = x
            py = y
        elif table[x][y] == 'Y':
            table[x][y] = '.'
            sx = x
            sy = y
        elif table[x][y] == 'T':
            table[x][y] = '.'
            ex = x
            ey = y

pirate_map()
danger_map()
bfs()
