#gold 2

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dijk(start):
    heap = []
    heappush(heap, (0, start))
    dist = [sys.maxsize for x in range(n + 1)]
    dist[start] = 0

    while heap:
        d, here = heappop(heap)
        for there, cost in table[here]:
            temp = d + cost
            if dist[there] > temp:
                dist[there] = temp
                heappush(heap, (temp, there))
    return dist


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    table = [[] for x in range(n + 1)]
    for x in range(m):
        a, b, d = map(int, input().split())
        table[a].append((b, d))
        table[b].append((a, d))

    candi = []
    for x in range(t):
        k = int(input())
        candi.append(k)
    candi.sort()

    s_dist = dijk(s)
    g_dist = dijk(g)
    h_dist = dijk(h)

    answer = []
    for can in candi:
        d1 = s_dist[g] + g_dist[h] + h_dist[can]
        d2 = s_dist[h] + h_dist[g] + g_dist[can]
        if d1 == s_dist[can] or d2 == s_dist[can]:
            answer.append(str(can))

    print(' '.join(answer))
