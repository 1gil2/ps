#gold 3

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = [0] + list(map(int,input().split()))
    indegree = [0 for x in range(n+1)]
    after = [[] for x in range(n+1)]
    ans = [0 for x in range(n+1)]
    for i in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        after[x].append(y)

    dq = deque()

    for x in range(1, n+1):
        if indegree[x] == 0:
            ans[x] = cost[x]
            dq.append(x)

    for x in range(1, n+1):
        cur = dq.popleft()
        for nxt in after[cur]:
            ans[nxt] = max(ans[nxt], ans[cur]+cost[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                dq.append(nxt)

    w = int(input())
    print(ans[w])