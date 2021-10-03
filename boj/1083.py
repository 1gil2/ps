#gold 4

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for x in range(n-1):
    if s == 0:
        break

    m = arr[x]
    idx = x
    e = min(n, x+s+1)

    for y in range(x+1, e):
        if m < arr[y]:
            m = arr[y]
            idx = y

    s -= idx - x

    for y in range(idx, x, -1):
        arr[y] = arr[y-1]

    arr[x] = m

print(*arr)
