#silver 4

import sys

n, m = map(int, sys.stdin.readline().split())

D = dict()

for x in range(n):
    a, b = sys.stdin.readline().split()
    D[a] = b

for x in range(m):
    a = input()
    print(D[a])
