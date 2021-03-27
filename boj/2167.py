#bronze 1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [list(map(int, input().split())) for x in range(n)]

dp = [[0 for y in range(m + 1)] for x in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, m + 1):
        dp[x][y] = table[x - 1][y - 1] + dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])

