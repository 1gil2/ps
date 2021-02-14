#bronze 3

A = input().split()
n = int(A[0])
x = int(A[1])
a = input().split()
for y in a:
    if int(y) < x:
        print(y, end=' ')
