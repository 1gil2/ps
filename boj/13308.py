#gold 1
#pypy3

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
costs = [0] + list(map(int, input().split()))

table = [[] for x in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

# dp[where][mcost] where까지 가는데 최소 기름값이 mcost 일때의 최소비용
dp = [[sys.maxsize for mcost in range(2501)] for where in range(n + 1)]
dp[1][costs[1]] = 0

heap = []
heappush(heap, (0, 1, costs[1]))

while heap:
    d, here, m = heappop(heap)

    if dp[here][m] < d:
        continue

    if here == n:
        print(d)
        break

    for there, dist in table[here]:
        temp = d + dist * m

        mm = min(m, costs[there])

        if dp[there][mm] > temp:
            dp[there][mm] = temp
            heappush(heap, (temp, there, mm))
