#gold 2

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
height = [0] + list(map(int, input().split()))

#dp[x][y] x에서 시작해서 y개의 다리를 건너서 도착할 수 있는 가장 낮은 높이 
dp = [[inf for y in range(501)] for x in range(n+1)]
for x in range(n+1):
    dp[x][0] = height[x]

tree = [[] for x in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

for y in range(1, 501):
    for x in range(1, n+1):
        for adj in tree[x]:
            dp[x][y] = min(dp[x][y], dp[adj][y-1])

t = int(input())
for _ in range(t):
    a, k = map(int, input().split())
    if dp[a][k] == inf:
        print(-1)
    else:
        print(dp[a][k])
