#gold 1

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]

# dp[x][y][k] x, y 의 최대값 k는 진입방향 0 위 1 왼 2 오
dp = [[[-sys.maxsize for z in range(3)] for y in range(m)] for x in range(n)]

ans = [[0 for y in range(m)] for x in range(n)]

ans[0][0] = table[0][0]

for x in range(1, m):
    ans[0][x] = ans[0][x - 1] + table[0][x]

for x in range(1, n):
    for y in range(m):
        dp[x][y][1] = ans[x - 1][y] + table[x][y]
        dp[x][y][2] = ans[x - 1][y] + table[x][y]

    for y in range(1, m):
        dp[x][y][1] = max(dp[x][y][1], dp[x][y - 1][1] + table[x][y])
    for y in range(m - 2, -1, -1):
        dp[x][y][2] = max(dp[x][y][2], dp[x][y + 1][2] + table[x][y])
    for y in range(m):
        ans[x][y] = max(dp[x][y][1], dp[x][y][2])

print(ans[n - 1][m - 1])
