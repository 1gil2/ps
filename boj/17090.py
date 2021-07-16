#gold 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def change(st):
    if st == 'U':
        return -1, 0
    elif st == 'D':
        return 1, 0
    elif st == 'R':
        return 0, 1
    elif st == 'L':
        return 0, -1


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1

    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 0

    dx, dy = change(table[x][y])
    visit[x][y] = dfs(x + dx, y + dy)

    return visit[x][y]


n, m = map(int, input().split())
table = [list(input().rstrip()) for x in range(n)]
visit = [[-1 for y in range(m)] for x in range(n)]
#visit[x][y] -1 not visit, 0 false, 1 true

cnt = 0
for x in range(n):
    for y in range(m):
        cnt += dfs(x, y)

print(cnt)
