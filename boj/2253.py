#gold 4

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())

v = int((2*n) ** 0.5) + 1

#dp[x][y] x번째 돌을 y칸 뛰어서 도착하는 경우의 수
dp = [[inf for y in range(v+1)] for x in range(n+1)]
dp[1][0] = 0
dp[2][1] = 1

stone = [True for x in range(n+1)]
for _ in range(m):
    s = int(input())
    stone[s] = False

for x in range(3, n+1):
    if not stone[x]:
        continue

    for y in range(1, v):
        dp[x][y] = min(dp[x-y][y-1], dp[x-y][y], dp[x-y][y+1]) + 1

ans = min(dp[n])

if ans == inf:
    print(-1)
else:
    print(ans)
