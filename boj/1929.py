#silver 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

prime = [False, False] + [True]*(m-1)
for x in range(2, m+1):
    if prime[x]:
        for y in range(2*x, m+1, x):
            prime[y] = False

for x in range(n, m+1):
    if prime[x]:
        print(x)
