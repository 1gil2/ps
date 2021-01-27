#gold 5

import sys
import math
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start):
    dist[start] = 0

    Q = []
    heappush(Q, (0, start))

    while Q:
        cost, here = heappop(Q)

        for there, cost2 in graph[here]:
            D = cost+cost2

            if dist[there] > D:
                dist[there] = D
                heappush(Q, (D, there))


n = int(input())
m = int(input())
graph = [[] for x in range(n + 1)]

dist = [math.inf for x in range(n + 1)]

for x in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

start, end = map(int, input().split())

dijkstra(start)
print(dist[end])
