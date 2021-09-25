#silver 5

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while n:
    if n&1:
        cnt += 1

    n >>= 1

print(cnt)
