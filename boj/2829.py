#gold 3
#pypy3

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for x in range(n)]

psum1 = [[0 for x in range(n+1)] for y in range(n+1)]
psum2 = [[0 for x in range(n+1)] for y in range(n+1)]

for x in range(n):
    for y in range(n):
        psum1[x+1][y+1] = psum1[x][y] + matrix[x][y]

for x in range(n):
    for y in range(n):
        psum2[x+1][n-y-1] = psum2[x][n-y] + matrix[x][n-y-1]

ans = 0
#x, y에서 시작하는 k*k 행렬에 대해서
for k in range(n):
    for x in range(n):
        for y in range(n):
            if x+k >= n or y+k >= n:
                continue
            A = psum1[x+k+1][y+k+1] - psum1[x][y]
            B = psum2[x+k+1][y] - psum2[x][y+k+1]
            ans = max(ans, A-B)

print(ans)
