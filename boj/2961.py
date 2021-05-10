#silver 1

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
item = []
for _ in range(n):
    item.append(list(map(int, input().split())))

ans = sys.maxsize
for k in range(1, n+1):
    combi = combinations(item, k)
    for com in combi:
        gob = 1
        hab = 0

        for g, h in com:
            gob *= g
            hab += h

        ans = min(ans, abs(gob-hab))

print(ans)
