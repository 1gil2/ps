#gold 4

import sys
input = sys.stdin.readline


def find(idx):
    if idx == parent[idx]:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


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
table = [list(map(int, input().split())) for x in range(n)]
travel = list(map(int, input().split()))

parent = [x for x in range(n)]
level = [1 for x in range(n)]

#만나면 union
for x in range(n):
    for y in range(n):
        if table[x][y] == 1:
            union(x, y)

#전 도시와 연결되어있는지 확인
post = travel[0]
flag = True
for city in travel:
    if find(post-1) != find(city-1):
        flag = False
        break
    post = city

if flag:
    print("YES")
else:
    print("NO")
