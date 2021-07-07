#gold 2

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijk(start):
    heap = []
    heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, here = heappop(heap)

        for there, cost in table[here]:
            temp = cost + d
            if dist[there] > temp:
                dist[there] = temp
                path[there] = here
                heappush(heap, (temp, there))


n, m = map(int, input().split())
table = [[] for x in range(n + 1)]
for x in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

path = [0 for x in range(n + 1)]
dist = [sys.maxsize for x in range(n + 1)]

dijk(1)

print(n - 1)
for x in range(2, n + 1):
    print(x, path[x])
