#gold 3
#pypy3

import sys

n = int(sys.stdin.readline())

M = 1 << 32

a, b = map(int, sys.stdin.readline().split())
mat = [a, b]
for x in range(n-1):
    b, c = map(int, input().split())
    mat.append(c)

dp = [[M for x in range(n)] for y in range(n)]

for x in range(n):
    dp[x][x] = 0

for x in range(1, n):
    for y in range(n-x):
        z = x+y
        for w in range(y, z):
            dp[y][z] = min(dp[y][z], dp[y][w]+dp[w+1][z]+mat[y-1]*mat[w]*mat[z])

print(dp[0][-1])
