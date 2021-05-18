#silver 2

import sys
input = sys.stdin.readline

d1, d2 = map(int, input().split())

s = set()

for x in range(d1, d2+1):
    for y in range(1, x+1):
        s.add(y/x)

print(len(s))
