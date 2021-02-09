#silver 1

import sys


def lcm(m, n):
    ans = m
    while True:
        if ans % n == 0:
            return ans
        ans += m


def kaing(m, n, x, y):
    x -= 1
    y -= 1
    lc = lcm(m, n)
    while x < lc:
        if x % n == y:
            return x+1
        x += m
    return -1


for x in range(int(sys.stdin.readline())):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(kaing(m, n, x, y))
