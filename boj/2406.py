#gold 3

import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [x for x in range(n+1)]

for x in range(m):
    a, b = map(int, input().split())
    union(a, b)

cost = [list(map(int, input().split())) for x in range(n)]

edges = []

for x in range(1, n):
    for y in range(x+1, n):
        edges.append((cost[x][y], x+1, y+1))

edges.sort()

x = 0
k = 0
answer = []
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer.append((a, b))
        x += c
        k += 1

print(x, k)
for a, b in answer:
    print(a, b)
