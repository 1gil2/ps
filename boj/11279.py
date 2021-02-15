#silver 2

import heapq
import sys

heap = []

n = int(sys.stdin.readline())
for x in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -a)
