#silver 3

T = int(input())
A = []
m = 0
for x in range(T):
    a = int(input())
    A.append(a)
    if m < a:
        m = a
D = [0, 1, 2, 4]
for x in range(4, m+1):
    D.append(D[x-3]+D[x-1]+D[x-2])

for x in A:
    print(D[x])
