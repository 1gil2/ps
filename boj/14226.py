#gold 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

s = int(input())

heap = []
heappush(heap, (0, 1, 0))
visit = [[0 for y in range(1001)] for x in range(1001)]
# visit[x][y] 현재 수 x, temp 수 y
visit[1][0] = 1

while heap:
    cnt, a, temp = heappop(heap)

    if a == s:
        print(cnt)
        break

    if visit[a][a] == 0:
        visit[a][a] = 1
        heappush(heap, (cnt + 1, a, a))

    if a > 0 and visit[a - 1][temp] == 0:
        visit[a - 1][temp] = 1
        heappush(heap, (cnt + 1, a - 1, temp))

    if a + temp < 1001 and visit[temp + a][temp] == 0:
        visit[a + temp][temp] = 1
        heappush(heap, (cnt + 1, a + temp, temp))
