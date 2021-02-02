#bronze 3

n = int(input())

for x in range(n):
    print('*' * (x+1))
for x in range(n-1):
    print('*' * (n-x-1))
