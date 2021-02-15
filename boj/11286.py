#silver 1

import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for x in range(n):
    k = int(sys.stdin.readline())
    if k != 0:
        heapq.heappush(heap, (abs(k), k))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
