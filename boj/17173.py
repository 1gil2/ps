#bronze 2

import sys

n, m = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

ans = 0
for x in range(n+1):
    for y in k:
        if x % y == 0:
            ans += x
            break
print(ans)
