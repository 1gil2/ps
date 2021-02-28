#silver 5
#pypy3

import math

n = int(input())

dp = [-1 for x in range(n+1)]
dp[0] = 0
dp[1] = 1

for x in range(2, n+1):
    m = 4
    k = int(math.sqrt(x))

    for y in range(1, k+1):
        temp = x-y*y
        m = min(m, dp[temp])

    dp[x] = m+1

print(dp[n])
