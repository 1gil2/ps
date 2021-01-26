#silver 2

def paper(x, y, N, A):
    for i in range(x, x + N):
        for j in range(y, y + N):
            if A[x][y] != A[i][j]:
                return False
    return True

def dc(x, y, N, A, B):
    if paper(x, y, N, A):
        B[A[x][y] + 1] += 1
        return
    k = N // 3
    for a in range(3):
        for b in range(3):
            dc(x + k * a, y + k * b, k, A, B)


N = int(input())
A = []
for x in range(N):
    A.append(list(map(int, input().split())))
B = [0, 0, 0]
dc(0, 0, N, A, B)
for x in B:
    print(x)
