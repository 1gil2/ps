#bronze 2

n = int(input())

for x in range(n):
    if x % 2 == 0:
        print("* "*n)
    else:
        print(" *"*n)
