#gold 2

import sys
input = sys.stdin.readline

n = int(input())
chu = list(map(int, input().split()))

m = int(input())
ball = list(map(int, input().split()))

dp = [[0 for y in range(40001)] for x in range(31)]

dp[0][0] = 1
dp[0][chu[0]] = 1

for x in range(1, n):
    for y in range(40001):
        if dp[x-1][y]:

            dp[x][y] = 1

            if 0 <= y+chu[x] < 40001:
                dp[x][y+chu[x]] = 1

            if 0 <= abs(y-chu[x]) < 40001:
                dp[x][abs(y-chu[x])] = 1

for b in ball:
    if dp[n-1][b] == 1:
        print("Y", end=' ')
    else:
        print("N", end=' ')
