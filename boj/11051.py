#silver 1

import sys

n, k = map(int, sys.stdin.readline().split())
d = [1]
for x in range(1, n+1):
    d.append(d[-1]*x)
print((d[n]//(d[k]*d[n-k])) % 10007)
