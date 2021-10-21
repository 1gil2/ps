#gold 4
#pypy3

import sys
input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]

psum = [[0 for y in range(m+1)] for x in range(n+1)]

for x in range(1, n+1):
    for y in range(1, m+1):
        psum[x][y] = table[x-1][y-1]

for x in range(1, n+1):
    for y in range(1, m+1):
        psum[x][y] = psum[x][y] + psum[x][y-1] + psum[x-1][y] - psum[x-1][y-1]

answer = -inf
for x in range(1, n+1):
    for y in range(1, m+1):
        for i in range(x, n+1):
            for j in range(y, m+1):
                answer = max(answer, psum[i][j] - psum[x-1][j] - psum[i][y-1] + psum[x-1][y-1])

print(answer)
