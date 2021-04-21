#gold 4

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))

table = [[sys.maxsize for y in range(n+1)] for x in range(n+1)]
for x in range(n+1):
    table[x][x] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    table[a][b] = c
    table[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            temp = table[i][k] + table[k][j]
            if table[i][j] > temp:
                table[i][j] = temp

ans = 0
for x in range(1, n+1):
    bucket = 0
    for y in range(1, n+1):
        if table[x][y] <= m:
            bucket += item[y]
    ans = max(ans, bucket)

print(ans)
