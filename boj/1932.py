#silver 1

import sys

n = int(sys.stdin.readline())
tri = []
for x in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1]*i for i in range(1, n+1)]
dp[0][0] = tri[0][0]

for x in range(1, n):
    for y in range(x+1):
        if y == 0:
            dp[x][y] = dp[x-1][y]+tri[x][y]
        elif y == x:
            dp[x][y] = dp[x-1][y-1]+tri[x][y]
        else:
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y])+tri[x][y]
print(max(dp[n-1]))
