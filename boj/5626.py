#platinum 4
#pypy3

import sys
input = sys.stdin.readline

inf = 1000000007
n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0 for y in range(10001)] for x in range(2)]
#dp[x][y] x까지의 높이 y까지의 경우의 수

if arr[1] < 1:
    dp[0][0] = 1

for x in range(2, n+1):
    for k in range(10001):
        dp[1][k] = 0

    if arr[x] == -1:
        dp[1][0] = (dp[0][0] + dp[0][1]) % inf
        for y in range(1, 5002):
            dp[1][y] = (dp[0][y-1] + dp[0][y] + dp[0][y+1]) % inf
    elif arr[x] == 0:
        dp[1][arr[x]] = (dp[0][arr[x]] + dp[0][arr[x]+1]) % inf
    else:
        dp[1][arr[x]] = (dp[0][arr[x]-1] + dp[0][arr[x]] + dp[0][arr[x]+1]) % inf

    for k in range(10001):
        dp[0][k] = dp[1][k]

print(dp[0][0])
