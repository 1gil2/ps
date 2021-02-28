#silver 3
#pypy3

import sys

n, q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
C = [0]
for x in A:
    C.append(C[-1]+x)
for x in range(q):
    a, b = map(int, sys.stdin.readline().split())
    print(C[b]-C[a-1])
