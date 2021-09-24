#silver 3

import sys
input = sys.stdin.readline

n = int(input())
le = len(str(n))

cnt = 0

for x in range(le-1):
    cnt += 9 * (10 ** x) * (x+1)

cnt += (n - 10 ** (le-1) + 1) * le

print(cnt)
