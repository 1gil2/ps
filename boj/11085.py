#gold 3

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


p, w = map(int, input().split())
c, v = map(int, input().split())

parent = [x for x in range(p)]

edges = []
for x in range(w):
    a, b, wi = map(int, input().split())
    edges.append((-wi, a, b))

edges.sort()

for wi, a, b in edges:
    union(a, b)

    if find(c) == find(v):
        print(-wi)
        break
