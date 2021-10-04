#gold 2

import sys
input = sys.stdin.readline


def go(n):
    arr = [0 for x in range(10)]
    ret = 0
    digit = 1

    while n > 0:
        a = n // (digit * 10)
        b = n % (digit * 10)

        for x in range(10):
            arr[x] += a * digit

        for x in range(1, b // digit + 1):
            arr[x] += digit

        arr[(b // digit + 1) % 10] += b % digit
        n -= 9 * digit
        digit *= 10

    for x in range(10):
        ret += x * arr[x]

    return ret


L, U = map(int, input().split())

print(go(U) - go(L - 1))
