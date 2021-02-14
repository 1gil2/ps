#silver 1

import sys

n, m = map(int, sys.stdin.readline().split())

table = []
for x in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for x in range(m+1)] for y in range(n+1)]

dp[1][1] = table[0][0]

for y in range(1, m+1):
    for x in range(1, n+1):
        dp[x][y] = table[x-1][y-1]+max(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])

print(dp[-1][-1])
