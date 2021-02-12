# gold 4

import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    AB = set()
    for x in A:
        for y in B:
            AB.add(x + y)
    AB = list(AB)
    AB.sort()

    CD = set()
    for x in C:
        for y in D:
            CD.add(x + y)
    CD = list(CD)
    CD.sort()

    M = -40000000
    cd_len = len(CD)

    for x in AB:
        idx = bisect.bisect_left(CD, k - x)

        if idx != 0:
            res = x + CD[idx - 1]
            if abs(k - M) > abs(k - res):
                M = res
            elif abs(k - M) == abs(k - res):
                M = min(M, res)
        if idx != cd_len:
            res = x + CD[idx]
            if abs(k - M) > abs(k - res):
                M = res
            elif abs(k - M) == abs(k - res):
                M = min(M, res)

    print(M)
