#gold 4

import sys
sys.setrecursionlimit(10**6)
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

for x in range(m):
    a, b, c = map(int, input().split())
    if a:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
    else:
        union(b, c)
