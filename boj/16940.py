#gold 3

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    dq = deque()
    dq.append(start)
    visit = [False for x in range(n+1)]
    visit[start] = True

    answer = [1]

    while dq:
        here = dq.popleft()
        for there in table[here]:
            if not visit[there]:
                visit[there] = True
                dq.append(there)
                answer.append(there)

    if answer == path:
        print(1)
    else:
        print(0)


n = int(input())
table = [[] for x in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)

path = list(map(int, input().split()))
order = [0 for x in range(n+1)]

for i, p in enumerate(path):
    order[p] = i

for i in range(1, n+1):
    table[i].sort(key = lambda x:order[x])

bfs(1)
