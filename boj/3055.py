#gold 5

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q.append([x1, y1])
    visit[x1][y1] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if table[nx][ny] == '.' and visit[nx][ny] == 0:
                        visit[nx][ny] = visit[x][y] + 1
                        q.append([nx, ny])
                    elif table[nx][ny] == 'D':
                        print(visit[x][y])
                        return
            qlen -= 1

        water()

    print("KAKTUS")
    return


def water():
    waterlen = len(water_q)
    while waterlen:
        x, y = water_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if table[nx][ny] == '.':
                    table[nx][ny] = '*'
                    water_q.append([nx, ny])
        waterlen -= 1


n, m = map(int, input().split())
table = [list(map(str, input())) for x in range(n)]
visit = [[0 for y in range(m)] for x in range(n)]

q = deque()
water_q = deque()

for x in range(n):
    for y in range(m):
        if table[x][y] == 'S':
            x1, y1 = x, y
            table[x][y] = '.'
        elif table[x][y] == '*':
            water_q.append([x, y])

water()
bfs()
