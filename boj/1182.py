#silver 2

import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int,input().split())
cnt = 0
arr = list(map(int,input().split()))

for x in range(1,n+1):
    temp = list(combinations(arr, x))
    for y in temp:
        if sum(y) == s:
            cnt += 1

print(cnt)
