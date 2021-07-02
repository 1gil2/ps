#gold 4

import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijk(start):
     heap = []
     heappush(heap, (0, start))
     ret = [sys.maxsize for x in range(n+1)]
     ret[start] = 0

     while heap:

          dist, here = heappop(heap)
          for there, cost in table[here]:

              temp = cost + dist

              if ret[there] > temp:
                  ret[there] = temp
                  heappush(heap, (temp, there))

     return ret


t = int(input())
for _ in range(t):
     n, d, s = map(int, input().split())
     table = [[] for x in range(n+1)]

     for i in range(d):
          a, b, c = map(int, input().split())
          table[b].append((a, c))

     dist = dijk(s)
     cnt = 0
     time = 0
     for d in dist:
          if d != sys.maxsize:
               if time < d:
                    time = d
               cnt += 1

     print(cnt, time)
