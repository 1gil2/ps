#gold 3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(here):
    for there in tree[here]:
        if not visit[there] and nutella[there] == 'R':
            visit[there] = True
            union(here, there)
            dfs(there)


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


n = int(input())
tree = [[] for x in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

nutella = input().rstrip()
parent = [x for x in range(n)]
size = [1 for x in range(n)]

visit = [False for x in range(n)]

for idx, color in enumerate(nutella):
    if color == 'R' and not visit[idx]:
        visit[idx] = True
        dfs(idx)

cnt = 0
for idx, color in enumerate(nutella):
    if color == 'B':
        for nxt in tree[idx]:
            if nutella[nxt] == 'R':
                cnt += size[find(nxt)]

print(cnt)
