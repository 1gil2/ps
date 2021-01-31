# gold 3

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

As = []
for x in range(n):
    s = A[x]
    As.append(s)
    for y in range(x + 1, n):
        s += A[y]
        As.append(s)

Bs = []
for x in range(m):
    s = B[x]
    Bs.append(s)
    for y in range(x + 1, m):
        s += B[y]
        Bs.append(s)

As.sort()
Bs.sort()

cnt = 0
for x in As:
    cnt += bisect_right(Bs, t - x) - bisect_left(Bs, t - x)

print(cnt)
