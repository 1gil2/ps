#gold 4

import sys
from bisect import bisect_left

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = a[::-1]

for _ in range(q):
    x, y = map(int, input().split())

    xx = max(0, a[y - 1] - x)

    idx = bisect_left(b, x, 0, n + 1 - y)
    yy = n - y - idx + 1

    print(xx + yy)
