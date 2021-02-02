#platinum 4

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, k = map(int, input().split())
bulb = list(map(int, input().split()))
my_bulb = []
for x in bulb:
    if my_bulb:
        if my_bulb[-1] != x:
            my_bulb.append(x)
    else:
        my_bulb.append(x)

lmb = len(my_bulb)
dp = [[0 for y in range(lmb)] for x in range(lmb)]

for x in range(lmb):
    for y in range(x-1, -1, -1):
        m = inf
        for k in range(y, x):
            temp = dp[y][k] + dp[k+1][x]

            if my_bulb[k] != my_bulb[x]:
                temp += 1

            if m > temp:
                m = temp

        dp[y][x] = m

print(dp[0][-1])
