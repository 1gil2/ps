#silver 3


def prinT():
    for x in range(m - 1):
        print(A[x], end=' ')
    print(A[-1])


def back(idx, length):
    if length == m:
        prinT()
        return

    for x in range(idx, n):
        A[length] = N[x]
        back(x, length + 1)


n, m = map(int, input().split())

N = list(range(1, n + 1))

A = [0] * m

back(0, 0)
