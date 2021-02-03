#silver 4

import math


def prime(n):
    a = 3
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    while a <= int(math.sqrt(n)):
        if n%a == 0:
            return 0
        a += 2
    return 1


m = int(input())
n = int(input())
total = 0
L = []

for x in range(m, n+1):
    if prime(x) == 1:
        L.append(x)
        total += x

if len(L) == 0:
    print(-1)
else:
    print(total)
    print(L[0])
