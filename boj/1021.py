#silver 4

import sys

n, m = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))
N = list(range(1, n+1))
cnt = 0
for x in d:
    a = N.index(x)
    l = len(N)
    if a == 0:
        N.pop(0)
    else:
        N = N[a:]+N[:a]
        if a-1 >= l//2:
            cnt += l-a
        else:
            cnt += a
        N.pop(0)

print(cnt)
