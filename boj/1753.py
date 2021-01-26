#gold 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
inf = 1000000007

v, e = map(int, input().split())
k = int(input())

dist = [inf for x in range(v+1)]
dist[k] = 0
table = [[] for x in range(v+1)]
heap = []
heappush(heap, (0, k))

for x in range(e):
    a, b, c = map(int, input().split())
    table[a].append([b, c])

while heap:
    a = heappop(heap)

    cost = a[0]
    here = a[1]

    lt = len(table[here])
    for x in range(lt):
        there = table[here][x][0]
        temp = table[here][x][1] + cost

        if dist[there] > temp:
            dist[there] = temp
            heappush(heap, (temp, there))

for x in range(1, v+1):
    if dist[x] == inf:
        print("INF")
    else:
        print(dist[x])
