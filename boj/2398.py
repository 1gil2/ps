#gold 1

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize


def dijk(idx, start):
    heap = []
    heappush(heap, (0, start))
    dist[idx][start] = 0

    while heap:
        d, here = heappop(heap)

        if dist[idx][here] < d:
            continue

        for there, cost in table[here]:
            temp = cost + d
            if dist[idx][there] > temp:
                dist[idx][there] = temp
                path[idx][there] = here
                heappush(heap, (temp, there))


n, m = map(int, input().split())

dist = [[inf for x in range(n + 1)] for y in range(3)]
path = [[0 for x in range(n + 1)] for y in range(3)]

table = [[] for x in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

people = list(map(int, input().split()))
for i, p in enumerate(people):
    dijk(i, p)

cnt = 0
station = 0
ans = inf

for x in range(n + 1):
    dd = dist[0][x] + dist[1][x] + dist[2][x]

    if ans > dd:
        station = x
        ans = dd

link = []
for i in range(3):
    s = station
    while s != people[i]:
        cnt += 1
        link.append((s, path[i][s]))
        s = path[i][s]

print(ans, cnt)
for a, b in link:
    print(a, b)
