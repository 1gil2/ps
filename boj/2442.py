#bronze 3

n = int(input())

for x in range(n):
    print(" "*(n-x-1), end='', sep='')
    print("*"*(2*x+1))
