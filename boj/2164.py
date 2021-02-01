#silver 4

import sys
import collections

n = int(sys.stdin.readline())
L = [x for x in range(1, n+1)]
deq = collections.deque(L)

for x in range(n-1):
    deq.popleft()
    deq.rotate(-1)
print(deq[0])
