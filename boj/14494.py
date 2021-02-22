#silver 1

import sys

n, m = map(int, sys.stdin.readline().split())

dp = [[0]*n for i in range(m)]

for x in range(m):
    dp[x][0] = 1
for x in range(n):
    dp[0][x] = 1

for x in range(1, m):
    for y in range(1, n):
        dp[x][y] = dp[x-1][y-1]+dp[x-1][y]+dp[x][y-1]

print(dp[-1][-1] % 1000000007)
