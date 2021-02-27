#silver 3

import sys

h, w, x, y = map(int, sys.stdin.readline().split())

A = [[-1]*w for i in range(h)]
B = []

for i in range(h+x):
    B.append(list(map(int, sys.stdin.readline().split())))

for i in range(x):
    for j in range(w):
        A[i][j] = B[i][j]

for i in range(x, h):
    for j in range(y):
        A[i][j] = B[i][j]

for i in range(x, h):
    for j in range(y, w):
        A[i][j] = B[i][j]-A[i-x][j-y]

for i in range(h):
    print(' '.join(map(str, A[i])))
