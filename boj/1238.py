#gold 3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijk(start):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[start] = 0

    heap = []
    heappush(heap, (0, start))

    while heap:
        d, here = heappop(heap)

        for there, cost in table[here]:
            D = d + cost
            if dist[there] > D:
                dist[there] = D
                heappush(heap, (D, there))

    return dist


n, m, x = map(int, input().split())
table = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))


back = dijk(x)

ans = 0
for k in range(1, n+1):
    ans = max(ans, dijk(k)[x]+back[k])

print(ans)
