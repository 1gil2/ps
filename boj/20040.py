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
parent = [x for x in range(n)]

for x in range(m):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)
    else:
        print(x+1)
        break
else:
    print(0)
