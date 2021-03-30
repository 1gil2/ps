#gold 2
#pypy3 top-down
#python3 bottom-up

import sys
input = sys.stdin.readline


def dtw(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = min(dtw(i-1, j-1), dtw(i, j-1), dtw(i-1, j)) + (x[i-1] - y[j-1])**2
    return dp[i][j]


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

'''
#더 빠름, 근데 top-down이 더 멋있음
dp = [[sys.maxsize for y in range(n+1)] for x in range(n+1)]
dp[0][0] = 0

for x in range(n):
    for y in range(n):
        dp[x+1][y+1] = min(dp[x][y+1], dp[x+1][y], dp[x][y]) + (a[x]-b[y]) ** 2

print(dp[-1][-1])
'''

#dp[i][j] x의 i, y의 j까지의 최소거리
dp = [[-1 for y in range(n+1)] for x in range(n+1)]

#초기값 세팅
dp[1][1] = (a[0] - b[0]) ** 2
for i in range(2, n+1):
    dp[1][i] = dp[1][i-1] + (a[0] - b[i-1]) ** 2
    dp[i][1] = dp[i-1][1] + (a[i-1] - b[0]) ** 2

print(dtw(n, n))
