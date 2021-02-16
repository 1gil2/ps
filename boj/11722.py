#silver 2

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0 for x in range(n)]

for x in range(n):
    for y in range(x):
        if A[x] < A[y]:
            dp[x] = max(dp[x], dp[y])
    dp[x] += 1

print(max(dp))
