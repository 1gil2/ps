#bronze 3

A = input().split()
a = int(A[0])
b = int(A[1])
c = int(A[2])
if a >= b >= c or a <= b <= c:
    print(b)
elif a >= c >= b or a <= c <= b:
    print(c)
else:
    print(a)
