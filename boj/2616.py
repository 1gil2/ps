#gold 4

import sys
input = sys.stdin.readline

n = int(input())
train = list(map(int, input().split()))
m = int(input())

psum = [0]
for t in train:
    psum.append(psum[-1] + t)

#dp[x][y] x소형기관차를 운용할 때 y객차가 마지막일때의 최대값
dp = [[0 for y in range(n+1)] for x in range(4)]

for x in range(1, 4):
    for y in range(x*m, n+1):
        if x == 1:
            dp[x][y] = max(dp[x][y-1], psum[y] - psum[y-m])
        else:
            dp[x][y] = max(dp[x][y-1], dp[x-1][y-m] + psum[y] - psum[y-m])

print(dp[3][n])
