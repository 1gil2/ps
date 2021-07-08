#gold 3

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

le1 = len(s1)
le2 = len(s2)

#dp[x][y] s1 x 까지로 s2 y 까지를 만드는 횟수
dp = [[0 for y in range(le2+1)] for x in range(le1+1)]

for x in range(le1+1):
    dp[x][0] = x

for y in range(le2+1):
    dp[0][y] = y

for x in range(1, le1+1):
    for y in range(1, le2+1):
        if s1[x-1] == s2[y-1]:
            dp[x][y] = dp[x-1][y-1]

        else:
            dp[x][y] = min(dp[x-1][y-1], dp[x][y-1], dp[x-1][y]) + 1

print(dp[le1][le2])
