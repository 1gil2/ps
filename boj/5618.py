#bronze 3
#pypy3

from math import gcd
import sys
input = sys.stdin.readline

n = int(input())

if n == 2:
    a, b = map(int, input().split())
    g = gcd(a, b)
elif n == 3:
    a, b, c = map(int, input().split())
    g = gcd(a, gcd(b, c))

for x in range(1, g//2+1):
    if g % x == 0:
        print(x)
print(g)
