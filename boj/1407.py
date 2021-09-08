#gold 4

import sys
input = sys.stdin.readline


def go(n):
    ret = n
    i = 2
    while i <= n:
        ret += (n//i)*(i//2)
        i *= 2

    return ret


a, b = map(int, input().split())

print(go(b) - go(a-1))
