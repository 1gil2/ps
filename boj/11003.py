#platinum 5
#pypy3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, l = map(int, input().split())
A = list(map(int, input().split()))
heap = []
answer = []

for i, a in enumerate(A):
    heappush(heap, (a, i))

    while heap[0][1] <= i-l:
        heappop(heap)

    answer.append(heap[0][0])

print(' '.join([str(x) for x in answer]))
