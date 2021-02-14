#silver 2

import bisect

n = int(input())
N = list(map(int, input().split()))
N.sort()

m = int(input())
M = list(map(int, input().split()))

for x in M:
    print(bisect.bisect_right(N, x)-bisect.bisect_left(N, x), end=' ')
