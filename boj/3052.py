#bronze 2

import sys

L = []
for x in range(10):
    a = int(sys.stdin.readline())
    if a % 42 not in L:
        L.append(a % 42)
print(len(L))
