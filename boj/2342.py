#gold 3

import sys
input = sys.stdin.readline


def power(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if a == 1:
        if b == 3:
            return 4
        return 3
    if a == 2:
        if b == 4:
            return 4
        return 3
    if a == 3:
        if b == 1:
            return 4
        return 3
    if a == 4:
        if b == 2:
            return 4
        return 3


cmd = list(map(int, input().split()))
dp = [[[0 for z in range(len(cmd))] for y in range(5)] for x in range(5)]
#[왼발][오른발][시행횟수]
dp[0][0][0] = 1
cnt = 0

for x in cmd:
    if x == 0:
        break
    for i in range(5):
        for j in range(5):
            if dp[i][j][cnt]:
                if dp[i][x][cnt + 1]:
                    dp[i][x][cnt + 1] = min(dp[i][x][cnt + 1], dp[i][j][cnt] + power(j, x))
                else:
                    dp[i][x][cnt + 1] = dp[i][j][cnt] + power(j, x)
                if dp[x][j][cnt + 1]:
                    dp[x][j][cnt + 1] = min(dp[x][j][cnt + 1], dp[i][j][cnt] + power(i, x))
                else:
                    dp[x][j][cnt + 1] = dp[i][j][cnt] + power(i, x)
    cnt += 1

M = 100000007
for i in range(5):
    for j in range(5):
        if dp[i][j][cnt]:
            M = min(M, dp[i][j][cnt])

print(M-1)
