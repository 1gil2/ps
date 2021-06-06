#silver 1

import sys
input = sys.stdin.readline


def cnt(x):
    ret = 0
    while x:
        ret += x%2
        x //= 2

    return ret


n, k = map(int, input().split())
nn = n

while True:
    temp = cnt(n)
    if temp <= k:
        print(n - nn)
        break
    else:
        n += 1
