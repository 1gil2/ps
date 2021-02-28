#silver 2

import sys

n = sys.stdin.readline()
N = list(map(int, sys.stdin.readline().split()))

Ns = list(set(N))
Ns.sort()

Nd = dict(zip(Ns, range(len(Ns))))

for x in N:
    print(Nd[x], end=' ')
