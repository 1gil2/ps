#silver 1

import sys

n = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

dp = [0]+P

for x in range(1, n+1):
    for y in range(1, x):
        dp[x] = max(dp[x-y]+P[y-1], dp[x])

print(dp[-1])
