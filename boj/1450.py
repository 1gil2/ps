#gold 1

import sys
from bisect import bisect_right
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
weights = list(map(int, input().split()))

bag1 = weights[:n//2]
bag2 = weights[n//2:]

le1 = len(bag1)
le2 = len(bag2)

can1 = [0]
for x in range(1, le1+1):
    for combi in combinations(bag1, x):
        can1.append(sum(combi))

can2 = [0]
for x in range(1, le2+1):
    for combi in combinations(bag2, x):
        can2.append(sum(combi))

can1.sort()
can2.sort()

cnt = 0

for cc in can1:
    if c < cc:
        continue
    cnt += bisect_right(can2, c-cc)

print(cnt)
