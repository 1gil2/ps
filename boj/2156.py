#silver 1

import sys

n = int(sys.stdin.readline())
wine = [0]
for x in range(n):
    wine.append(int(sys.stdin.readline()))

dp = [0]
dp.append(wine[1])
if n >= 3:
    dp.append(dp[-1] + wine[2])
    for x in range(3, n + 1):
        dp.append(max(wine[x] + dp[x - 2], dp[x - 1], wine[x] + wine[x - 1] + dp[x - 3]))
    print(dp[-1])
else:
    print(sum(wine))
