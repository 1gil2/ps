#silver 1

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

heap = []

n = int(input())
for x in range(n):
    a = int(input())
    if a == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, a)
