#gold 4

import sys
input = sys.stdin.readline
mod = 10007

n = int(input())

#dp[x][y][z] x층에 기웅, 민수 좌표가 (y, z)있을 경우의 수
dp = [[[0 for minsu in range(101)] for gi in range(101)] for level in range(101)]

dp[2][1][2] = 1

for level in range(2, n):
    for x in range(1, level):
        for y in range(x+1, level+1):
            dp[level+1][x][y] = (dp[level+1][x][y] + dp[level][x][y]) % mod
            dp[level+1][x+1][y+1] = (dp[level+1][x+1][y+1] + dp[level][x][y]) % mod
            dp[level+1][x][y+1] = (dp[level+1][x][y+1] + dp[level][x][y]) % mod

            if x+1 != y:
                dp[level+1][x+1][y] = (dp[level+1][x+1][y] + dp[level][x][y]) % mod

ans = 0
for x in range(n+1):
    for y in range(n+1):
        ans += dp[n][x][y]

print((ans * 2) % mod)
