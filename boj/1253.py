#gold 4

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = defaultdict(int)
for a in arr:
    cnt[a] += 1

num = defaultdict(int)
for x in range(n):
    if arr[x] == 0:
        continue
    for y in range(x+1, n):
        if arr[y] == 0:
            continue
        num[arr[x]+arr[y]] += 1

if cnt[0]:
    if cnt[0] > 2:
        num[0] += 1
    for key, val in cnt.items():
        if key != 0 and val > 1:
            num[key] += 1

answer = 0
for a in arr:
    if num[a]:
        answer += 1

print(answer)
