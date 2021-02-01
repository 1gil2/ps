#gold 5

import sys
from math import factorial as fac
input = sys.stdin.readline

n, r = map(int, input().split())
print(int(fac(n+r-1)//(fac(r-1)*fac(n)))%1000000000)
