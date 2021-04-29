#gold 2

import sys
from collections import deque
input = sys.stdin.readline


def move():
    # 상어 순회 및 이동
    where = []
    for x in range(r):
        for y in range(c):
            if table[x][y]:
                where.append((x, y))

    R = 2 * r - 2
    C = 2 * c - 2
    for x, y in where:
        s, d, z = table[x][y].popleft()
        # d : 1 위 2 아래 3 오 4 왼
        if d == 1:
            x = (R - x + s) % R
            if x >= r:
                table[R - x][y].append((s, 1, z))
            else:
                table[x][y].append((s, 2, z))
        elif d == 2:
            x = (x + s) % R
            if x >= r:
                table[R - x][y].append((s, 1, z))
            else:
                table[x][y].append((s, 2, z))
        elif d == 4:
            y = (C - y + s) % C
            if y >= c:
                table[x][C - y].append((s, 4, z))
            else:
                table[x][y].append((s, 3, z))
        elif d == 3:
            y = (y + s) % C
            if y >= c:
                table[x][C - y].append((s, 4, z))
            else:
                table[x][y].append((s, 3, z))

    # 먹고 먹히기
    for x in range(r):
        for y in range(c):
            if len(table[x][y]) > 1:
                temp = max(table[x][y], key=lambda x: x[2])
                table[x][y] = deque([temp])


r, c, m = map(int, input().split())
table = [[deque() for y in range(c)] for x in range(r)]

for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    table[i - 1][j - 1].append((s, d, z))

user = -1
ans = 0
while user < c - 1:
    # 낚시왕 이동
    user += 1

    # 상어 잡기
    for x in range(r):
        if table[x][user]:
            shark = table[x][user].pop()
            ans += shark[2]
            break

    # 상어 이동
    move()

print(ans)
