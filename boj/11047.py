#silver 1

import sys

n, k = map(int, sys.stdin.readline().split())
d = []
for x in range(n):
    d.append(int(sys.stdin.readline()))
cnt = 0
while k > 0:
    if d[n-1] <= k:
        a = k//d[n-1]
        k -= d[n-1]*a
        cnt += a
    n -= 1
print(cnt)
