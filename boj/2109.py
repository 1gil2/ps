#gold 3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
pd = []
for _ in range(n):
    p, d = map(int, input().split())
    pd.append((p, d))

pd.sort(key=lambda x: x[1])

heap = []
for p, d in pd:
    heappush(heap, p)

    if len(heap) > d:
        heappop(heap)

print(sum(heap))
