#silver 3

import sys

k, n = map(int, sys.stdin.readline().split())

N = []

for x in range(k):
    a = int(sys.stdin.readline())
    N.append(a)

N.sort()

m = 1
M = N[-1]

while m <= M:
    mid = (m+M)//2

    cnt = sum([(i//mid) for i in N])

    if cnt >= n:
        ans = mid
        m = mid+1
    elif cnt < n:
        M = mid-1

print(ans)
