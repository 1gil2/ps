#silver 1


def Aprint(n):
    for x in range(n):
        for y in range(n):
            print(A[x][y], end='')
        print()


def table(n, a, b):
    if n == 1:
        A[a][b] = '*'
    else:
        for x in range(3):
            for y in range(3):
                if x != 1 or y != 1:
                    table(n//3, a+(n//3)*x, b+(n//3)*y)


n = int(input())
A = [[' ' for x in range(n)] for y in range(n)]
table(n, 0, 0)
Aprint(n)
