#gold 5

import sys
import heapq

n = int(sys.stdin.readline())
h = [0]
for i in map(int, sys.stdin.readline().split()):
    h += [i+b for b in h]

n = 0
h = list(set(h))
hep = []
for x in h:
    heapq.heappush(hep, x)

while True:
    if len(hep) == 0:
        print(n)
        break
    k = heapq.heappop(hep)
    if k == n:
        n += 1
    else:
        print(n)
        break
