#gold 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for x in range(n):
    a = list(map(int, input().rstrip()))
    table.append(a)

for x in range(1, n):
    for y in range(1, m):
        if table[x][y]:
            table[x][y] += min(table[x - 1][y - 1], table[x - 1][y], table[x][y - 1])

ans = 0
for x in range(n):
    for y in range(m):
        ans = max(ans, table[x][y])

print(ans * ans)

