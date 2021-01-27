#silver 5

import sys


def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)


for x in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(a*b//gcd(a, b))
