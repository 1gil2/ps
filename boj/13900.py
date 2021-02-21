#silver 4

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
s = 0
for x in A:
    s += x
result = 0
for x in A:
    result += (s-x)*x
print(result//2)
