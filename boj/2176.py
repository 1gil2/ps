#gold 2

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize


def dijk(start):
    heap = []
    heappush(heap, (0, 2))
    dist[2] = 0
    dp[2] = 1

    while heap:
        d, here = heappop(heap)

        if dist[here] < d:
            continue

        for there, cost in table[here]:
            temp = d + cost

            if dist[there] > temp:
                dist[there] = temp
                heappush(heap, (temp, there))

            if dist[there] < d:
                dp[here] += dp[there]


n, m = map(int, input().split())

table = [[] for x in range(n + 1)]
dist = [inf for x in range(n + 1)]
# dp[x] x번 노드에서 출발하는 합리적인 이동경로 수
dp = [0 for x in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

dijk(2)
print(dp[1])
