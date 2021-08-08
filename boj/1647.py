#gold 4

import sys
input = sys.stdin.readline


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


n, m = map(int, input().split())
parent = [x for x in range(n+1)]

edges = []
for x in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans = 0
for edge in edges:
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        ans += edge[0]
        temp = edge[0]

print(ans - temp)
