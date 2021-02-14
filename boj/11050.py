#bronze 1

import sys

n, k = map(int, sys.stdin.readline().split())
ans = 1
for x in range(k+1, n+1):
    ans *= x
for x in range(1, n-k+1):
    ans //= x
print(ans)
