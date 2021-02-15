#gold 4

import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[math.inf for x in range(n + 1)] for y in range(n + 1)]
for x in range(n + 1):
    dist[x][x] = 0

for x in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for z in range(1, n + 1):
            if y != z:
                dist[y][z] = min(dist[y][z], dist[y][x] + dist[x][z])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if dist[x][y] == math.inf:
            dist[x][y] = 0

for x in range(1, n + 1):
    for y in range(1, n + 1):
        print(dist[x][y], end=' ')
    print()
