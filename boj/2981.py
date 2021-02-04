#silver 1

import math

n = int(input())
num = []
ans = []

for x in range(n):
    num.append(int(input()))

num.sort()

g = num[1]-num[0]

for x in range(1, n):
    g = math.gcd(g, num[x]-num[x-1])

sq = int(math.sqrt(g))

ans.append(g)
for x in range(2, sq+1):
    if g % x == 0:
        ans.append(x)
        ans.append(g//x)

ans = list(set(ans))
ans.sort()

for x in ans:
    print(x, end=' ')
