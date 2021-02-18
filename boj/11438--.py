#platinum 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(idx, dep):
    visit[idx] = 1
    depth[idx] = dep

    for nxt in v[idx]:
        if visit[nxt]:
            continue
        parent[nxt][0] = idx
        dfs(nxt, dep+1)


def LCA(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for x in range(16, -1, -1):
        if (depth[b] - depth[a]) >= (1 << x):
            b = parent[b][x]

    if a == b:
        return a

    for x in range(16, -1, -1):
        if parent[a][x] != parent[b][x]:
            a = parent[a][x]
            b = parent[b][x]

    return parent[a][0]


n = int(input())

parent = [[0 for y in range(17)] for x in range(n+1)]
#parent[x][y] 정점 x의 2^y 번째 조상 정점 번호
depth = [0 for x in range(n+1)]
v = [[] for x in range(n+1)]
visit = [0 for x in range(n+1)]

for x in range(n-1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

dfs(1, 0)

for y in range(1, 17):
    for x in range(1, n+1):
        parent[x][y] = parent[parent[x][y-1]][y-1]

m = int(input())
for x in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))
