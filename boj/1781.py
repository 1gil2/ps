#gold 2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
problems = []

for x in range(n):
    dead, ramen = map(int, input().split())
    problems.append((dead, ramen))

problems.sort()

heap = []

for i, problem in enumerate(problems):
    heappush(heap, problem[1])

    if problem[0] < len(heap):
        heappop(heap)

print(sum(heap))
