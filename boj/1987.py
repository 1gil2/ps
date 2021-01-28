#gold 4
#pypy3

import sys


def dfs(x, y, l):
    global ans
    ans = max(ans, l)

    for d in range(4):
        x1 = x + dx[d]
        y1 = y + dy[d]
        if 0 <= x1 < r and 0 <= y1 < c and visit[table[x1][y1]] == 0:
            visit[table[x1][y1]] = 1
            dfs(x1, y1, l + 1)
            visit[table[x1][y1]] = 0


r, c = map(int, sys.stdin.readline().split())

table = [[0 for x in range(c)] for y in range(r)]

for x in range(r):
    st = sys.stdin.readline()

    for y in range(c):
        table[x][y] = ord(st[y]) - 65

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [0] * 26
ans = 0

visit[table[0][0]] = 1
dfs(0, 0, 1)
print(ans)
