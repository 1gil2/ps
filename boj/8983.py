#gold 4

import sys
from bisect import bisect_left
input = sys.stdin.readline

m, n, l = map(int, input().split())
base = list(map(int, input().split()))
base.sort()

ans = 0

for _ in range(n):
    #가장 가까운 사대를 찾아서 확인
    x, y = map(int, input().split())
    idx = bisect_left(base, x)

    if idx == 0:
        if abs(x-base[idx]) + y <= l:
            ans += 1
    elif idx == m:
        if abs(x-base[idx-1]) + y <= l:
            ans += 1
    else:
        if abs(x-base[idx]) + y <= l or abs(x-base[idx-1]) + y <= l:
            ans += 1

print(ans)
