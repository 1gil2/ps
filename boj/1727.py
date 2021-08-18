#gold 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

men = list(map(int, input().split()))
women = list(map(int, input().split()))

men.sort()
women.sort()

#dp[x][y] 남자 x 여자 y 까지의 최솟값
dp = [[0 for y in range(m+1)] for x in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        temp = dp[x-1][y-1] + abs(men[x-1] - women[y-1])
        if x > y:
            dp[x][y] = min(temp, dp[x-1][y])
        elif x < y:
            dp[x][y] = min(temp, dp[x][y-1])
        else:
            dp[x][y] = temp

print(dp[n][m])
