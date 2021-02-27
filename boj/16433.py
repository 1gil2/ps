#bronze 1

n, r, c = map(int, input().split())

if (r+c) % 2 == 0:
    for x in range(n):
        if x % 2 == 0:
            print("v."*(n//2), sep='', end='')
            if n % 2 == 1:
                print("v")
            else:
                print()
        else:
            print(".v"*(n//2), sep='', end='')
            if n % 2 == 1:
                print(".")
            else:
                print()
else:
    for x in range(n):
        if x % 2 == 1:
            print("v."*(n//2), sep='', end='')
            if n % 2 == 1:
                print("v")
            else:
                print()
        else:
            print(".v"*(n//2), sep='', end='')
            if n % 2 == 1:
                print(".")
            else:
                print()
