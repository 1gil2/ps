#gold 4

import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(here):
    if visit[here] == 0:
        visit[here] = 1
        for there, dis in tree[here]:
            if visit[there] == 0:
                dist[there] = dist[here]+dis
                dfs(there)


n = int(input())

tree = [[] for x in range(n+1)]

for x in range(n-1):
    a, b, c = map(int,input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

dist = [0 for x in range(n+1)]
visit = [0 for x in range(n+1)]
dfs(1)
m = 0
idx = 0
for x in range(n+1):
    if dist[x] > m:
        m = dist[x]
        idx = x

dist = [0 for x in range(n+1)]
visit = [0 for x in range(n+1)]
dfs(idx)
print(max(dist))
