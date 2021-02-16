#silver 3

import sys

n, m = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
ps = [0]
for x in L:
    ps.append(ps[-1]+x)
for x in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(ps[b]-ps[a-1])
