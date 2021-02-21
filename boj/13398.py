#gold 5

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for y in range(2)] for x in range(n+1)]

ans = arr[0]

for x in range(n):
    dp[x][0] = arr[x]
    dp[x][1] = arr[x]

for x in range(1, n):
    dp[x][0] = max(dp[x][0], dp[x-1][0] + arr[x])
    dp[x][1] = max(dp[x-1][0], dp[x-1][1]+arr[x])
    ans = max(ans, dp[x][0], dp[x][1])

print(ans)
