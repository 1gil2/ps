#gold 1

import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
nodes = []
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z, i))

edges = []
for i in range(3):
    nodes.sort(key=lambda x:x[i])
    for j in range(n-1):
        edges.append((abs(nodes[j][i] - nodes[j+1][i]), nodes[j][3], nodes[j+1][3]))
edges.sort()

parent = [x for x in range(n)]
ans = 0

for edge in edges:
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        ans += edge[0]

print(ans)
