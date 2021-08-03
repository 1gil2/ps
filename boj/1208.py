#gold 2

import sys
from itertools import combinations
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

arr1 = nums[:n//2]
arr2 = nums[n//2:]

le1 = len(arr1)
le2 = len(arr2)

sum1 = []
sum2 = []

for x in range(1, le1+1):
    for combi in combinations(arr1, x):
        sum1.append(sum(combi))

for x in range(1, le2+1):
    for combi in combinations(arr2, x):
        sum2.append(sum(combi))

sum1.sort()
sum2.sort()

cnt += bisect_right(sum1, s) - bisect_left(sum1, s)
cnt += bisect_right(sum2, s) - bisect_left(sum2, s)

for left in sum1:
    cnt += bisect_right(sum2, s-left) - bisect_left(sum2, s-left)

print(cnt)
