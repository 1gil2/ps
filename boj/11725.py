#silver 2

import sys
sys.setrecursionlimit(10 ** 9)


def dfs(idx, par):
    if parent[idx] == 0:
        parent[idx] = par
        for x in D[idx]:
            dfs(x, idx)


n = int(input())

D = dict()
parent = [0 for x in range(n + 1)]
parent[0] = 1
parent[1] = 1
for x in range(n + 1):
    D[x] = []

for x in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    D[a].append(b)
    D[b].append(a)

s = 1

for x in D[s]:
    dfs(x, s)

for x in range(2, n + 1):
    print(parent[x])
