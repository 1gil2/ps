#gold 2

import sys
input = sys.stdin.readline

n, s = map(int, input().split())

pictures = [[0, 0]] + [list(map(int, input().split())) for x in range(n)]
pictures.sort()

#dp[x] x번째 그림이 제일 위에 보일때 최댓값
dp = [0 for x in range(n+1)]
dp[1] = pictures[1][1]
ans = dp[1]

temp = 0
idx = 0

for x in range(1, n+1):
    while pictures[idx][0] <= pictures[x][0] - s:
        temp = max(temp, dp[idx])
        idx += 1

    dp[x] = temp + pictures[x][1]
    ans = max(ans, dp[x])

print(ans)
