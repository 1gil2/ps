#silver 2

import sys
sys.setrecursionlimit(10**6)


def dfs(a):
    visit[a] = 1
    for x in range(1, n+1):
        if table[a][x] == 1 and visit[x] == 0:
            dfs(x)


n, m = map(int, sys.stdin.readline().split())

table = [[0 for x in range(n+1)] for x in range(n+1)]

for x in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[a][b] = 1
    table[b][a] = 1

visit = [0 for x in range(n+1)]
visit[0] = 1

cnt = 0

for x in range(1, n+1):
    if visit[x] == 0:
        cnt += 1
        dfs(x)

print(cnt)
