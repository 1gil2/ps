#gold 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize


def dijk():
    heap = []
    heappush(heap, (0, 0))

    dist = [inf for x in range(m)]
    dist[0] = 0
    path = [[] for x in range(m)]
    path[0].append(0)

    while heap:
        d, here = heappop(heap)

        if dist[here] < d:
            continue

        for there, cost in table[here]:
            temp = cost + d

            if dist[there] > temp:
                dist[there] = temp
                heappush(heap, (temp, there))
                path[there] = []
                for p in path[here]:
                    path[there].append(p)
                path[there].append(there)

    if dist[m - 1] == inf:
        print(f'Case #{tt + 1}: -1')
    else:
        print(f'Case #{tt + 1}:', *path[m - 1])


t = int(input())
for tt in range(t):
    n, m = map(int, input().split())

    table = [[] for x in range(m)]

    for x in range(n):
        a, b, c = map(int, input().split())
        table[a].append((b, c))
        table[b].append((a, c))

    dijk()
