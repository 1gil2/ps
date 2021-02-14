#silver 5

import sys

so = [0]*10000
n = int(sys.stdin.readline())

for x in range(n):
    so[int(sys.stdin.readline())-1] += 1

for x in range(10000):
    [print(x+1) for y in range(so[x])]
