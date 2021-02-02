#gold 4
#pypy3

import sys
input = sys.stdin.readline
inf = 100000007

n, m = map(int, input().split())

table = [[inf for y in range(n+1)] for x in range(n+1)]
p = [0 for x in range(n+1)]

for x in range(1, n+1):
    table[x][x] = 0

for x in range(m):
    a, b = map(int, input().split())
    table[a][b] = 1

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            table[x][y] = min(table[x][y], table[x][k]+table[k][y])

for x in range(1, n+1):
    for y in range(1, n+1):
        if table[x][y] != inf and x != y:
            p[x] += 1
            p[y] += 1

ans = 0
for x in range(1, n+1):
    if p[x] == n-1:
        ans += 1

print(ans)
