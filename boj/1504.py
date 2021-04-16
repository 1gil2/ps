#gold 4

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(start, end):
    D = [inf for x in range(n+1)]
    D[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        dist, here = heappop(heap)

        for there, cost in table[here]:
            temp = dist + cost
            if D[there] > temp:
                D[there] = temp
                heappush(heap, (temp, there))

    return D[end]


n, e = map(int, input().split())
table = [[] for x in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
dist2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

ans = min(dist1, dist2)

if ans >= inf:
    print(-1)
else:
    print(min(dist1, dist2))
