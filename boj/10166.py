#silver 2

import sys
from math import gcd
input = sys.stdin.readline

d1, d2 = map(int, input().split())
visit = [0 for x in range(2001)]

ans = 1
for i in range(d1, d2+1):
    check = []
    for j in range(1, i):
        g = gcd(i, j)

        if visit[i//g]:
            continue

        ans += 1
        check.append(i//g)

    for c in check:
        visit[c] = 1

print(ans)
