#silver 4

import bisect

N = input()
A = list(map(int, input().split()))
M = input()
B = list(map(int, input().split()))

A.sort()

for b in B:
    if A[bisect.bisect(A, b)-1] == b:
        print(1)
    else:
        print(0)
