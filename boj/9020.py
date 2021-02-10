#silver 1
#pypy3

import bisect

for _ in range(int(input())):
    a = int(input())

    num = [False, False]+[True]*(a-1)
    prime = []
    for x in range(2, a+1):
        if num[x]:
            prime.append(x)
            for y in range(2*x, a+1, x):
                num[y] = False

    b = a//2
    c = bisect.bisect_left(prime, b)
    while True:
        if num[a-prime[c]]:
            break
        c += 1
    print(a-prime[c], prime[c])
