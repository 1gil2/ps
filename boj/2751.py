#silver 5
#pypy3

n = int(input())

A = []

for x in range(n):
    A.append(int(input()))

A.sort()

for x in range(n):
    print(A[x])
