#bronze 2

import sys
input = sys.stdin.readline

s, k = map(int, input().split())

prime = [True for x in range(k+1)]
prime[0] = False
prime[1] = False

for x in range(2, int(k**0.5)+1):
    if prime[x]:
        for y in range(2*x, k+1, x):
            if prime[y]:
                prime[y] = False

flag = False
ans = 0

for x in range(2, k):
    if prime[x] and s%x == 0:
        flag = True
        ans = x
        break

if flag:
    print("BAD", ans)
else:
    print("GOOD")
