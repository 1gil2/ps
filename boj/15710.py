#gold 4

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

mod = 1000000007


def power(a, b):
    ret = 1
    while b > 0:
        if b%2 == 1:
            ret = (ret*a)%mod

        a = (a*a)%mod
        b //= 2

    return ret%mod


a, b, n = map(int, input().split())
print(power(power(2, 31), n-1))
