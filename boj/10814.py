#silver 5

n = int(input())

A = []

for x in range(n):
    a, b = input().split()
    A.append([int(a), x, b])

A.sort()

for x in range(n):
    print(A[x][0], A[x][2])
