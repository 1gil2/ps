#platinum 5
#pypy3

import sys
from bisect import bisect_right
input = sys.stdin.readline

n, m, k = map(int, input().split())
minsu = list(map(int, input().split()))
chulsu = list(map(int, input().split()))

minsu.sort()

visit = [False for x in range(m)]

for card in chulsu:
    idx = bisect_right(minsu, card)

    while visit[idx]:
        idx += 1

    visit[idx] = True

    print(minsu[idx])
