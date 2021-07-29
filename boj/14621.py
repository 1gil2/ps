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


n, m = map(int, input().split())

mw = ['X'] + list(map(str, input().split()))

parent = [x for x in range(n + 1)]
roads = []

for x in range(m):
    u, v, d = map(int, input().split())
    roads.append((d, u, v))

roads.sort()

ans = 0
cnt = 0
for road in roads:
    x = find(road[1])
    y = find(road[2])
    if x == y:
        continue
    elif mw[road[1]] != mw[road[2]]:
        union(x, y)
        ans += road[0]
        cnt += 1

if cnt == n - 1:
    print(ans)
else:
    print(-1)
