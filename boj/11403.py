#silver 1

import math

n = int(input())

G = [list(map(int, input().split())) for x in range(n)]

for i in range(n):
    for j in range(n):
        if G[i][j] == 0:
            G[i][j] = math.inf

for k in range(n):
    for i in range(n):
        for j in range(n):
            G[i][j] = min(G[i][j], G[i][k]+G[k][j])

for i in range(n):
    for j in range(n):
        if G[i][j] == math.inf:
            G[i][j] = '0'
        else:
            G[i][j] = '1'

for x in range(n):
    print(" ".join(G[x]))
