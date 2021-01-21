#silver2

import sys

st = sys.stdin.readline().split('-')

part = []

for x in st:
    temp = list(map(int, x.split('+')))
    part.append(sum(temp))

ans = part[0]

for x in part[1:]:
    ans -= x

print(ans)
