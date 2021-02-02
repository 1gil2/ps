#bronze 3

n = int(input())

for x in range(n):
    print(" " * x, end='')
    print("*" * (2*n-1-2*x))
for x in range(n-2, -1, -1):
    print(" " * x, end='')
    print("*" * (2*n-1-2*x))
