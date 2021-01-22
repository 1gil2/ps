#silver 2

from math import gcd
import sys
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
c, d = a1*b2+a2*b1, b1*b2
g = gcd(c, d)
print(c//g, d//g)
