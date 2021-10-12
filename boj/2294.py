#silver 1

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, k = map(int, input().split())
coins = [int(input()) for x in range(n)]
coins.sort()

dp = [inf for x in range(k+1)]
dp[0] = 0

for coin in coins:
    for x in range(coin, k+1):
        dp[x] = min(dp[x], dp[x - coin] + 1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])
