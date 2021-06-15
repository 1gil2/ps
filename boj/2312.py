#silver 2

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    for x in range(2, n+1):
        cnt = 0

        if n % x == 0:
            while n % x == 0:
                n //= x
                cnt += 1

            print(x, cnt)

        elif n == 1:
            break
