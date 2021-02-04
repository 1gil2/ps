#silver 4

import sys

n, k = map(int, sys.stdin.readline().split())

prime = [False, False]+[True]*(n-1)
cnt = 0

for x in range(2, n+1):
    for y in range(x, n+1, x):
        if prime[y]:
            cnt += 1
            if cnt == k:
                print(y)
                break
        prime[y] = False
    if cnt == k:
        break
