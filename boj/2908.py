#bronze 2

A, B = input().split()
a = int(A[::-1])
b = int(B[::-1])
if a < b:
    print(b)
else:
    print(a)
