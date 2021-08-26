#platinum 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize

n, d = map(int, input().split())
k = list(map(int, input().split()))

dp = k[:]

heap = []
heappush(heap, (-dp[0], 0))

for x in range(1, n):
    while heap[0][1] < x-d:
        heappop(heap)

    dp[x] = max(dp[x], k[x] - heap[0][0])
    heappush(heap, (-dp[x], x))

print(max(dp))