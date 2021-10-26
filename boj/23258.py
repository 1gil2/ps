#gold 1
#pypy3

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, q = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]

#dist[x][y][z] 1~x번 정점만 사용해서 만드는 플로이드와샬
dist = [[[inf for z in range(n+1)] for y in range(n+1)] for x in range(n+1)]

for x in range(n):
    for y in range(n):
        if table[x][y] == 0 and x != y:
            dist[0][x+1][y+1] = inf
        else:
            dist[0][x+1][y+1] = table[x][y]

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            dist[k][x][y] = min(dist[k-1][x][y], dist[k-1][x][k] + dist[k-1][k][y])

for _ in range(q):
    c, s, e = map(int, input().split())
    if dist[c-1][s][e] == inf:
        print(-1)
    else:
        print(dist[c-1][s][e])
