# gold 4

import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if level[a] > level[b]:
        a, b = b, a

    parent[a] = b

    if level[a] == level[b]:
        level[b] += 1


n = int(input())
m = int(input())

parent = [x for x in range(n + 1)]
level = [1 for x in range(n + 1)]
cost = []

for x in range(m):
    a1, a2, a3 = map(int, input().split())
    cost.append([a3, a1, a2])

cost.sort()

ans = 0
cnt = 0
for i in range(m):
    x = find(cost[i][1])
    y = find(cost[i][2])
    if x == y:
        continue
    else:
        union(x, y)
        ans += cost[i][0]
        cnt += 1
    if cnt == n - 1:
        print(ans)
        break
