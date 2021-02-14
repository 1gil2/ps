#silver 1

import sys

input = sys.stdin.readline

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
dp = [[0]*(n+1) for x in range(n+1)]
#dp[x][y] 오른쪽 x장, 왼쪽 y장 남았을 때 최대 점수

for x in range(n-1, -1, -1):
    for y in range(n-1, -1, -1):
        if right[y] < left[x]:
            dp[x][y] = max(dp[x][y+1]+right[y], dp[x+1][y], dp[x+1][y+1])
        else:
            dp[x][y] = max(dp[x+1][y], dp[x+1][y+1])

print(dp[0][0])
