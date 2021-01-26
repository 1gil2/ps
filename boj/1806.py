#gold 4

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
j = t = 0
r = 0
for i in range(n):
    t += a[i]
    while t >= m:
        t -= a[j]
        j += 1
    if r == 0 or r > i-j+2 and j > 0:
        r = i-j+2
print(r)
