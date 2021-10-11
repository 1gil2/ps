#gold 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize


def dijk(start):
    dist = [inf for x in range(v + 1)]
    dist[start] = 0
    heap = []
    heappush(heap, (0, start))

    while heap:
        d, here = heappop(heap)

        if dist[here] < d:
            continue

        for there, cost in table[here]:
            temp = d + cost
            if dist[there] > temp:
                dist[there] = temp
                heappush(heap, (temp, there))

    return dist


n, v, e = map(int, input().split())
a, b = map(int, input().split())

team = list(map(int, input().split()))

table = [[] for x in range(v + 1)]

for _ in range(e):
    x, y, z = map(int, input().split())
    table[x].append((y, z))
    table[y].append((x, z))

dist1 = dijk(a)
dist2 = dijk(b)

answer = 0
for t in team:
    if dist1[t] == inf:
        answer -= 1
    else:
        answer += dist1[t]

    if dist2[t] == inf:
        answer -= 1
    else:
        answer += dist2[t]

print(answer)
