#silver 5

import sys
fac = [1]
for x in range(1, 31):
    fac.append(fac[-1]*x)
for x in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    print(fac[m]//(fac[n]*fac[m-n]))
