#gold 4

import math


def catalan(n):
    return math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))


t = int(input())
for x in range(t):
    a = int(input())
    if a % 2 == 0:
        print(catalan(a//2) % 1000000007)
    else:
        print(0)
