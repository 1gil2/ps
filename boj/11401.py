#gold 1

import sys
sys.setrecursionlimit(10 ** 6)

MOD = 1000000007


def power(a, b):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans = (ans * a) % MOD
        a = (a * a) % MOD
        b = b // 2
    return ans % MOD


def fac(a):
    ans = 1
    for x in range(2, a + 1):
        ans = (ans * x) % MOD
    return ans


def bi(a, b):
    if a == b or b == 0:
        return 1
    x = fac(a)
    y = fac(b)
    z = fac(a - b)
    return x * power((y * z) % MOD, MOD - 2) % MOD


n, k = map(int, input().split())

print(bi(n, k))
