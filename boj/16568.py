#silver 1

import sys

n, a, b = map(int, sys.stdin.readline().split())

if a > b:
    a, b = b, a

dp = [x for x in range(n+1)]

for x in range(1, n+1):
    if x > a:
        dp[x] = min(dp[x-a-1]+1, dp[x])
    if x > b:
        dp[x] = min(dp[x-b-1]+1, dp[x])

print(dp[-1])
