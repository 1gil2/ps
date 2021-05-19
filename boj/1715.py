#gold 4

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
ans = 0

for x in range(n):
    heappush(heap, int(input()))

while True:
    if len(heap) == 1:
        print(ans)
        break

    a = heappop(heap)
    b = heappop(heap)
    ans += a + b
    heappush(heap, a+b)
