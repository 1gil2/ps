#silver 2

import bisect

while True:
    a = int(input())
    if a == 0:
        break

    num = [False, False]+[True]*(2*a-1)
    prime = []
    for x in range(2, 2*a+1):
        if num[x]:
            prime.append(x)
            for y in range(2*x, 2*a+1, x):
                num[y] = False

    print(len(prime)-bisect.bisect(prime, a))
