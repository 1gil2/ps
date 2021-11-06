#gold 4

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
table = [[inf for y in range(n+1)] for x in range(n+1)]
for x in range(n+1):
    table[x][x] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    table[u][v] = 0
    if b == 0:
        table[v][u] = 1
    else:
        table[v][u] = 0

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            temp = table[x][k] + table[k][y]
            if table[x][y] > temp:
                table[x][y] = temp

q = int(input())
for _ in range(q):
    s, e = map(int, input().split())
    print(table[s][e])
