#bronze 2

A = []
for x in range(9):
    A.append(int(input()))

x = max(A)
print(x)
print(A.index(x)+1)
