#silver 1

import sys

n, m = map(int, sys.stdin.readline().split())
table = []
for x in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

pstab = [[0]*(n+1) for x in range(n+1)]
for x in range(1, n+1):
    for y in range(1, n+1):
        pstab[x][y] = pstab[x-1][y]+pstab[x][y-1]+table[x-1][y-1]-pstab[x-1][y-1]

for x in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(pstab[x2][y2]-pstab[x1-1][y2]-pstab[x2][y1-1]+pstab[x1-1][y1-1])
