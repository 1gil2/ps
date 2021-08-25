#gold 3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

stations = [tuple(map(int, input().split())) for x in range(n)]
stations.sort()

end, power = map(int, input().split())
stations.append((end, 0))

heap = []

cnt = 0
here = 0
for d, gas in stations:
    power -= d - here

    while power < 0:
        if not heap:
            print(-1)
            sys.exit()

        power -= heappop(heap)
        cnt += 1

    heappush(heap, -gas)
    here = d

print(cnt)
