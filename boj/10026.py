#gold 5

import sys
sys.setrecursionlimit(1000000)


def dfs1(x, y):
    p1[x][y] = 1
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
            continue
        elif table[x + dx][y + dy] == table[x][y] and p1[x + dx][y + dy] == 0:
            dfs1(x + dx, y + dy)


def dfs2(x, y):
    p2[x][y] = 1
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
            continue
        elif table2[x + dx][y + dy] == table2[x][y] and p2[x + dx][y + dy] == 0:
            dfs2(x + dx, y + dy)


n = int(input())

table = [list(input()) for x in range(n)]

p1 = [[0] * n for i in range(n)]
p2 = [[0] * n for i in range(n)]

cnt1 = 0
cnt2 = 0

for x in range(n):
    for y in range(n):
        if p1[x][y] == 0:
            dfs1(x, y)
            cnt1 += 1

table2 = table
for x in range(n):
    for y in range(n):
        if table[x][y] == 'G':
            table2[x][y] = 'R'

for x in range(n):
    for y in range(n):
        if p2[x][y] == 0:
            dfs2(x, y)
            cnt2 += 1
print(cnt1, cnt2)
