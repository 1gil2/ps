#silver 1


def qud(x, y, N, A):
    if N == 1:
        print(A[y][x], end='')
        return
    for i in range(y, y + N):
        for j in range(x, x + N):
            if A[y][x] != A[i][j]:
                print("(", end='')
                qud(x, y, N // 2, A)
                qud(x + N // 2, y, N // 2, A)
                qud(x, y + N // 2, N // 2, A)
                qud(x + N // 2, y + N // 2, N // 2, A)
                print(")", end='')
                return
    print(A[y][x], end='')


N = int(input())
A = []
for x in range(N):
    A.append(list(input()))

qud(0, 0, N, A)
