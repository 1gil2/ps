#gold 2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline


n, m = map(int, input().split())
problems = [[] for x in range(n+1)]
indeg = [0 for x in range(n+1)]

for x in range(m):
    a, b = map(int, input().split())
    problems[a].append(b)
    indeg[b] += 1

heap = []
for x in range(1, n+1):
    if indeg[x] == 0:
        heappush(heap, x)

ans = []
while heap:
    node = heappop(heap)
    ans.append(str(node))
    for x in problems[node]:
        indeg[x] -= 1
        if indeg[x] == 0:
            heappush(heap, x)

print(' '.join(ans))
