#platinum 5
#pypy3

import sys
from math import log2
from collections import deque
input = sys.stdin.readline

n = int(input())
mx = int(log2(n) + 1)
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [[0 for _ in range(mx)] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
vis = [0 for _ in range(n+1)]

q = deque()
q.append(1)
while q:
    nd = q.popleft()
    vis[nd] = 1
    for nxt in adj[nd]:
        if not vis[nxt]:
            vis[nxt] = 1
            q.append(nxt)
            parent[nxt][0] = nd
            depth[nxt] = depth[nd] + 1

for j in range(1, mx):
    for i in range(1, n+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]

    for i in range(mx):
        if diff & 1 << i:
            u = parent[u][i]

    if u == v:
        print(u)
        continue

    for i in range(mx-1, -1, -1):
        if parent[u][i] != parent[v][i]:
            u, v = parent[u][i], parent[v][i]
    print(parent[u][0])
