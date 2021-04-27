#gold 5

import sys

n = int(input())

if n == 1:
    print(0)
    sys.exit()

#dp[n][k] n자리 수 중에 나머지가 k인 경우의 수
dp = [[0 for y in range(3)] for x in range(n+1)]

dp[1][1] = 1
dp[1][2] = 1

for x in range(2, n+1):
    dp[x][0] = (dp[x-1][1] + dp[x-1][2])%1000000007
    dp[x][1] = (dp[x-1][0] + dp[x-1][2])%1000000007
    dp[x][2] = (dp[x-1][0] + dp[x-1][1])%1000000007

print(dp[n-1][1]%1000000007)
