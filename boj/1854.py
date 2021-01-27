#platinum 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 1000000007

n, m, k = map(int, input().split())
dist = [[] for x in range(n+1)]
heappush(dist[1], 0)
table = [[] for x in range(n+1)]
heap = []
heappush(heap, [0, 1])

for x in range(m):
    a, b, c = map(int, input().split())
    table[a].append([b, c])

while heap:
    cost, here = heappop(heap)

    for there, cost2 in table[here]:
        temp = cost+cost2
        if len(dist[there]) < k:
            heappush(dist[there], -temp)
            heappush(heap, [temp, there])
        elif dist[there][0] < -temp:
            heappop(dist[there])
            heappush(dist[there], -temp)
            heappush(heap, [temp, there])

for x in range(1, n+1):
    if len(dist[x]) >= k:
        print(-dist[x][0])
    else:
        print(-1)
