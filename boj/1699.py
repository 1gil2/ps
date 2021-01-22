#silver 3

import math

n = int(input())

dp = [x for x in range(n+1)]

dp[1] = 1

for x in range(2, n+1):
    k = int(math.sqrt(x))
    for y in range(k+1):
        if dp[x] > dp[x-y*y]+1:
            dp[x] = dp[x-y*y]+1

print(dp[n])
