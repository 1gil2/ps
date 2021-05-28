#gold 2

import sys
input = sys.stdin.readline


def solve(a):
    if a == 0:
        return 0

    le = 0
    b = a
    while b:
        b //= 2
        le += 1

    temp = a - (2 ** (le-1))
    return int((le-1) * (2 ** (le-2)) + temp + 1 + solve(temp))


n, m = map(int, input().split())

print(solve(m) - solve(n-1))
