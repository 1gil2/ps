#gold 3

import sys
input = sys.stdin.readline

n = int(input())
children = list(map(int, input().split()))

dp = [0 for x in range(n+1)]

for child in children:
    dp[child] = dp[child-1] + 1

print(n - max(dp))
