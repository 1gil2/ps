#gold 2

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indeg = [0 for x in range(n + 1)]
table = [[] for x in range(n + 1)]

for _ in range(m):
    pd = list(map(int, input().split()))
    le = pd[0]
    prog = pd[1:]

    pre = prog[0]
    for i, x in enumerate(prog):
        if i == 0:
            continue
        indeg[x] += 1
        table[pre].append(x)
        pre = x

dq = deque()
for x in range(1, n + 1):
    if indeg[x] == 0:
        dq.append(x)

answer = []
flag = True
for x in range(n):
    if not dq:
        flag = False
        break

    cur = dq.popleft()
    answer.append(cur)

    for nxt in table[cur]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            dq.append(nxt)

if flag:
    for a in answer:
        print(a)
else:
    print(0)
