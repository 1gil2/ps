#platinum 5

import sys
from heapq import heappush, heappop
from collections import deque

input = sys.stdin.readline


def bfs(end):
    dq = deque()
    dq.append(end)

    while dq:
        here = dq.popleft()

        for there in range(n):
            if dist[here] == dist[there] + table[there][here] and table[there][here] != -1:
                table[there][here] = -1
                dq.append(there)


def dijk(start):
    heap = []
    heappush(heap, (0, start))

    while heap:
        dis, here = heappop(heap)

        for there in range(n):
            if table[here][there] == -1:
                continue

            temp = dis + table[here][there]

            if dist[there] > temp:
                dist[there] = temp
                heappush(heap, (temp, there))


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    s, d = map(int, input().split())

    table = [[-1 for y in range(n + 1)] for x in range(n + 1)]

    for x in range(m):
        u, v, p = map(int, input().split())
        table[u][v] = p

    dist = [sys.maxsize for x in range(n + 1)]
    dist[s] = 0

    dijk(s)

    bfs(d)

    dist = [sys.maxsize for x in range(n + 1)]
    dist[s] = 0

    dijk(s)

    if dist[d] == sys.maxsize:
        print(-1)
    else:
        print(dist[d])
