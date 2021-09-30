#gold 4

import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 1]

if n < 2:
    print(dp[n])
else:
    for x in range(2, n+1):
        if x%2:
            dp.append(dp[-1]*2 - 1)
        else:
            dp.append(dp[-1]*2 + 1)

    print(dp[n])
