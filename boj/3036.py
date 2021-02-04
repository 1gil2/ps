#silver 3

import math

n = int(input())

ring = list(map(int, input().split()))

r = ring[0]

for x in range(1, n):
    g = math.gcd(r, ring[x])
    print(r//g, end='')
    print("/", end='')
    print(ring[x]//g)
