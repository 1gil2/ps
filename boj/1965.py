#silver 2

import sys
input = sys.stdin.readline

n = int(input())
boxs = list(map(int, input().split()))

dp = [1 for x in range(n)]

for x in range(1, n):
    for y in range(x):
        if boxs[x] > boxs[y]:
            dp[x] = max(dp[x], dp[y]+1)

print(max(dp))
