#gold 4

import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

div = []
for x in range(1, int(sqrt(n)) + 1):
    if n % x == 0:
        div.append(x)

ans = []
for d in div:
    if d == n // d:
        continue

    if (d + n // d) % 2 == 0:
        ans.append((d + n // d) // 2)

ans.sort()
if ans:
    for a in ans:
        print(a)
else:
    print(-1)
