#gold 4

import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for x in range(n)]

ans = sys.maxsize

# 첫번째 집 색깔 0: r, 1: g, 2: b
for i in range(3):
    # dp[x][y] x번째 집의 색이 y일 때의 최솟값
    dp = [[sys.maxsize for y in range(3)] for x in range(n + 1)]

    # x가 1일때(초기값)
    dp[1][i] = rgb[0][i]

    # x가 2 ~ n-1
    for x in range(2, n):
        dp[x][0] = min(dp[x - 1][1], dp[x - 1][2]) + rgb[x - 1][0]
        dp[x][1] = min(dp[x - 1][0], dp[x - 1][2]) + rgb[x - 1][1]
        dp[x][2] = min(dp[x - 1][0], dp[x - 1][1]) + rgb[x - 1][2]

    for y in range(3):
        if y == i:
            continue
        for z in range(3):
            if y == z:
                continue
            dp[n][y] = min(dp[n][y], dp[n - 1][z] + rgb[n - 1][y])

    ans = min(ans, dp[n][0], dp[n][1], dp[n][2])

print(ans)
