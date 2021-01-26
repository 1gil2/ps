#platinum 5

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())

for x in range(m):
    a, b, c = map(int, input().split())