#gold 2

import sys
input = sys.stdin.readline

move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


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
table = [input().strip() for x in range(n)]

parent = [x for x in range(n*m)]

for i in range(n*m):
    x = i//m
    y = i%m
    dx, dy = move[table[x][y]]

    x1 = x + dx
    y1 = y + dy

    union(i, x1*m + y1)

s = set()
for p in parent:
    s.add(find(p))

print(len(s))
