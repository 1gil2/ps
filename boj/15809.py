#gold 4

import sys
input = sys.stdin.readline
inf = sys.maxsize


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
        power[x] += power[y]
    else:
        parent[x] = y
        power[y] += power[x]


def war(x, y):
    x = find(x)
    y = find(y)

    if power[x] == power[y]:
        parent[x] = 0
        parent[y] = 0
    elif power[x] > power[y]:
        power[x] -= power[y]
        parent[y] = x
    else:
        power[y] -= power[x]
        parent[x] = y


n, m = map(int, input().split())
parent = [x for x in range(n+1)]
power = [0 for x in range(n+1)]

for x in range(1, n+1):
    power[x] = int(input())

for _ in range(m):
    o, p, q = map(int, input().split())
    if o == 1:
        union(p, q)
    else:
        war(p, q)

remain = [False for x in range(n+1)]
for x in range(1, n+1):
    remain[find(x)] = True

cnt = 0
ans = []
for x in range(1, n+1):
    if remain[x]:
        cnt += 1
        ans.append(power[x])

ans.sort()

print(cnt)
print(*ans)
