#silver 4

import sys
import math
input = sys.stdin.readline

n = int(input())
for x in range(n):
    a, b = map(int, input().split())
    print(a*b//math.gcd(a, b))
