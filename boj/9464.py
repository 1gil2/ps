#gold 1
#pypy 3

import sys
from math import gcd

input = sys.stdin.readline

s = set()
for y in range(1, 710):
    for x in range(y + 1, 710):
        a = 2 * x * y
        b = x * x - y * y
        c = x * x + y * y

        if a * a + b * b != c * c:
            continue

        g = gcd(a, gcd(b, c))
        a //= g
        b //= g

        if a > b:
            a, b = b, a

        s.add((a + b, a, b))

s = list(s)
s.sort()

t = int(input())
for _ in range(t):
    le = int(input())

    cnt = 0
    for c, x, y in s:
        cost = 2 * c

        if le >= cost:
            le -= cost
            cnt += 1

    print(cnt)
