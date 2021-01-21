#silver 2

import sys
from collections import deque

def dfs(x):
    if visit[x] == 1:
        return
    visit[x] = 1
    for y in range(1, n+1):
        if(visit[y] == 0 and table[x][y] == 1):
            print(y, end=' ')
            dfs(y)

n, m, v = map(int, sys.stdin.readline().split())

table = [[0 for x in range(n+1)]for y in range(n+1)]
visit = [0 for x in range(n+1)]

for x in range(m):
    a, b = map(int, sys.stdin.readline().split())
    table[a][b] = 1
    table[b][a] = 1

print(v, end=' ')
dfs(v)
print()

visit = [0 for x in range(n+1)]
que = [v]
dq = deque(que)
visit[v] = 1
print(v, end=' ')
while dq:
    a = dq.popleft()
    for x in range(1, n+1):
        if(visit[x] == 0 and table[a][x] == 1):
            dq.append(x)
            visit[x] = 1
            print(x, end=' ')