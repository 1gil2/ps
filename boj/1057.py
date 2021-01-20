#silver 3

import sys

m, n, k = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    cnt += 1
    m = m//2
    n = (n+1)//2
    k = (k+1)//2
    if n == k:
        break
print(cnt)
