#gold 2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
jew = []
for x in range(n):
    heappush(jew, list(map(int, input().split())))

bags = []
for x in range(k):
    bags.append(int(input()))

bags.sort()

answer = 0
temp = []

for bag in bags:
    while jew and bag >= jew[0][0]:
        heappush(temp, -jew[0][1])
        heappop(jew)

    if temp:
        answer -= heappop(temp)
    elif not jew:
        break

print(answer)
