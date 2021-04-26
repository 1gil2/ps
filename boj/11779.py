#gold 3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dijk(s, e):
    dist = [sys.maxsize for x in range(n + 1)]
    dist[s] = 0

    heap = []
    heappush(heap, (0, s))

    while heap:
        d, here = heappop(heap)

        for there, cost in table[here]:
            D = cost + d

            if dist[there] > D:
                dist[there] = D
                heappush(heap, (D, there))
                path[there] = []
                for p in path[here]:
                    path[there].append(p)
                path[there].append(there)

    return dist[e]


n = int(input())
m = int(input())

table = [[] for x in range(n + 1)]
path = [[] for x in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))

s, e = map(int, input().split())
path[s].append(s)

visit = [0 for x in range(n + 1)]
visit[s] = 1

ans = dijk(s, e)

print(ans)
print(len(path[e]))
print(' '.join(map(str, path[e])))
