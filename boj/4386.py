#gold 4

import sys
from math import sqrt

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


n = int(input())
parent = [x for x in range(n + 1)]

stars = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

edges = []
for x in range(n - 1):
    for y in range(x + 1, n):
        edges.append((sqrt((stars[x][0] - stars[y][0]) ** 2 + (stars[x][1] - stars[y][1]) ** 2), x, y))

edges.sort()

ans = 0
for cost, x, y in edges:

    if find(x) != find(y):
        union(x, y)
        ans += cost

print(round(ans, 2))
