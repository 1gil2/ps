#gold 4

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < m and 0 <= y1 < n:
            if table[x1][y1] < table[x][y]:
                dp[x][y] += dfs(x1, y1)

    return dp[x][y]

m, n = map(int, input().split())
table = [list(map(int, input().split())) for x in range(m)]
dp = [[-1 for y in range(n)] for x in range(m)]

print(dfs(0, 0))
