#gold 5

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [[0 for y in range(21)] for x in range(n+1)]

dp[0][num[0]] = 1
for x in range(1, n):
    for y in range(0, 21):
        if dp[x-1][y]:
            if y+num[x] <= 20:
                dp[x][y+num[x]] += dp[x-1][y]
            if y-num[x] >= 0:
                dp[x][y-num[x]] += dp[x-1][y]

print(dp[n-2][num[-1]])
