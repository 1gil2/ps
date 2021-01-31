#silver 4
#pypy3

from collections import Counter

n = int(input())

su = 0
m = n//2
L = []
for x in range(n):
    a = int(input())
    su += a
    L.append(a)

L.sort()

L2 = Counter(L).most_common()

print(round(su/n))

print(L[m])

if len(L2) > 1:
    if L2[0][1] == L2[1][1]:
        print(L2[1][0])
    else:
        print(L2[0][0])
else:
    print(L2[0][0])

if n == 1:
    print(0)
else:
    print(L[-1]-L[0])
