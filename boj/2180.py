#gold 1

import sys
from functools import cmp_to_key
input = sys.stdin.readline


def my_compare(x, y):
    if x[0] == 0:
        return 1
    elif y[0] == 0:
        return -1
    elif x[1] == 0 and y[1] == 0:
        if x[0] > y[0]:
            return 1
        else:
            return -1

    if x[1] * y[0] > x[0] * y[1]:
        return 1
    return -1


n = int(input())

sb = []
for x in range(n):
    sobang = list(map(int, input().split()))
    sb.append(sobang)

sb.sort(key=cmp_to_key(my_compare))

ans = 0
for s in sb:
    ans += (s[0] * ans + s[1]) % 40000

print(ans % 40000)
