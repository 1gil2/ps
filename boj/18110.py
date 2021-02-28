#silver 4

import sys
input=sys.stdin.readline


def my_round(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    return int(n)


n = int(input())

if n == 0:
    print(0)
else:
    A = []
    for x in range(n):
        A.append(int(input()))
    A.sort()
    a = my_round(n*15/100)
    print(my_round(sum(A[a:n-a])/(n-2*a)))
