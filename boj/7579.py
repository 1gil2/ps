#gold 3

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0 for y in range(10001)] for x in range(101)]
#dp[x][y] x번째까지 사용해서 y코스트를 써서 확보할 수 있는 메모리의 최댓값

ans = sys.maxsize
for x in range(1, n+1):
    for y in range(10000):
        if cost[x] > y:
            dp[x][y] = dp[x-1][y]
        else:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-cost[x]]+memory[x])
        if dp[x][y] >= m:
            ans = min(ans, y)

print(ans)
