#gold 1

import sys
input = sys.stdin.readline


def dfs(here):
    if visit[here] == 0:
        visit[here] = 1
        for there, dis in tree[here]:
            if visit[there] == 0:
                dist[there] = dist[here] + dis
                dfs(there)


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, k = map(int, input().split())
parent = [x for x in range(n)]

tree = [[] for x in range(n)]
dist = [0 for x in range(n)]
visit = [0 for x in range(n)]

edges = []
for x in range(k):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans1 = 0
for c, a, b in edges:
    if find(a) != find(b):
        tree[a].append((b, c))
        tree[b].append((a, c))
        union(a, b)
        ans1 += c

dfs(0)
m = 0
idx = 0
for x in range(n):
    if dist[x] > m:
        m = dist[x]
        idx = x

dist = [0 for x in range(n)]
visit = [0 for x in range(n)]
dfs(idx)

print(ans1)
print(max(dist))
