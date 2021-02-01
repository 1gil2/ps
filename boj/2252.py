# gold 2

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indeg = [0 for x in range(n + 1)]
after = [[] for x in range(n + 1)]
for x in range(m):
    a, b = map(int, input().split())
    indeg[b] += 1
    after[a].append(b)

dq = deque()
for x in range(1, n + 1):
    if indeg[x] == 0:
        dq.append(x)

for x in range(1, n + 1):
    cur = dq.popleft()
    print(cur, end=' ')
    for nxt in after[cur]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            dq.append(nxt)
