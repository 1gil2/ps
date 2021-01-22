#gold 2

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []

for x in range(n):
    a = int(input())
    if x == 0:
        heappush(max_heap, -a)
        print(a)
        continue

    if len(max_heap) == len(min_heap):
        if a > min_heap[0]:
            heappush(max_heap, -heappop(min_heap))
            heappush(min_heap, a)
        else:
            heappush(max_heap, -a)
    else:
        if a < -max_heap[0]:
            heappush(min_heap, -heappop(max_heap))
            heappush(max_heap, -a)
        else:
            heappush(min_heap, a)

    print(-max_heap[0])
