# silver 2

import sys
input = sys.stdin.readline


def pf(a):
    res = 1
    for i in p:
        cnt = 0
        if a % i == 0:
            while a % i == 0:
                cnt += 1
                a //= i

            res *= i ** cnt - i ** (cnt - 1)
    return res


p = []
prime = [False, False] + [True for x in range(1001)]
for x in range(2, 1001):
    if prime[x]:
        p.append(x)
        for y in range(2 * x, 1001, x):
            if prime[y]:
                prime[y] = False

c = int(input())
for x in range(c):
    ans = 0
    n = int(input())
    for y in range(1, n + 1):
        ans += pf(y)
    print(2 * ans + 1)
