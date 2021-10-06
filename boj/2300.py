#gold 3
#pypy3

import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
dp = [inf for x in range(n+1)]

xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, abs(y)))

xy.sort()

dp[0] = 0
dp[1] = xy[0][1] * 2

for i in range(2, n+1):
    maxh = 0
    for j in range(i-1, -1, -1):
        maxh = max(maxh, xy[j][1])
        dp[i] = min(dp[i], dp[j] + max(maxh * 2, xy[i-1][0] - xy[j][0]))

print(dp[n])
