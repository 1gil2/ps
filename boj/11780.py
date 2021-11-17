#gold 2

import sys

input = sys.stdin.readline
inf = sys.maxsize


def go(x, y):
    if path[x][y] == 0:
        return []

    k = path[x][y]
    return go(x, k) + [k] + go(k, y)


n = int(input())
m = int(input())

table = [[inf for y in range(n + 1)] for x in range(n + 1)]
path = [[0 for y in range(n + 1)] for x in range(n + 1)]

for x in range(n + 1):
    table[x][x] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a][b] = min(table[a][b], c)

for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            temp = table[x][k] + table[k][y]
            if table[x][y] > temp:
                table[x][y] = temp
                path[x][y] = k

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if table[x][y] == inf:
            print(0, end=' ')
        else:
            print(table[x][y], end=' ')
    print()

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if table[x][y] == 0 or table[x][y] == inf:
            print(0)
        else:
            temp = [x] + go(x, y) + [y]
            print(len(temp), *temp)
