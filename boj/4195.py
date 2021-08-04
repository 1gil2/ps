#gold 2

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

    if x > y:
        x, y = y, x

    if x != y:
        parent[y] = x
        size[x] += size[y]


t = int(input())
for _ in range(t):
    f = int(input())
    parent = dict()
    size = dict()
    for i in range(f):
        p1, p2 = map(str, input().strip().split())
        if p1 not in parent:
            parent[p1] = p1
            size[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            size[p2] = 1
        union(p1, p2)

        print(size[find(p1)])
