#bronze 1

import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for x in range(n)]
L.sort()

for x in L:
    print(x)
