#gold 1

import sys

n = int(sys.stdin.readline())
dp = [[0 for y in range(1024)]for x in range(10)]

for x in range(1, 10):
    dp[x][1<<x] = 1 #dp[마지막 숫자][비트마스킹으로 사용된 숫자 파악]

for x in range(1, n):
    dp1 = [[0 for y in range(1024)] for x in range(10)]
    for y in range(10):
        for z in range(1024):
            if y < 9:
                dp1[y][z | (1<<y)] = (dp1[y][z | (1<<y)]+dp[y+1][z])%1000000000
            if y > 0:
                dp1[y][z | (1<<y)] = (dp1[y][z | (1<<y)]+dp[y-1][z])%1000000000
    dp = dp1

su = 0
for x in range(10):
    su += dp[x][1023]

print(su%1000000000)
