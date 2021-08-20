#gold 4
#pypy3

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
table = [[sys.maxsize for y in range(v+1)] for x in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    table[a][b] = c

for x in range(v+1):
    table[x][x] = 0

for k in range(1, v+1):
    for x in range(1, v+1):
        for y in range(1, v+1):
            temp = table[x][k] + table[k][y]
            if table[x][y] > temp:
                table[x][y] = temp

ans = sys.maxsize
for x in range(1, v+1):
    for y in range(1, v+1):
        if x == y:
            continue
        ans = min(ans, table[x][y] + table[y][x])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
