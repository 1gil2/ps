#gold 3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
work = [0 for x in range(1001)]

for x in range(n):
    d, w = map(int, input().split())
    heappush(heap, (-w, d))

while heap:
    point, day = heappop(heap)
    for x in range(day, 0, -1):
        if work[x] == 0:
            work[x] = -point
            break

print(sum(work))
