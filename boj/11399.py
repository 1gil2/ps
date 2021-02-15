#silver 3

import sys

n = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))
print(sum([a[i]*(n-i)for i in range(n)]))
