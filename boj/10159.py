#gold 3

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

table = [[0 for x in range(n)] for y in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1

for k in range(n):
    for x in range(n):
        for y in range(n):
            if table[x][k] and table[k][y]:
                table[x][y] = 1

for x in range(n):
    cnt = 0
    for y in range(n):
        if table[x][y] == 0 and table[y][x] == 0:
            cnt += 1
    print(cnt-1)
