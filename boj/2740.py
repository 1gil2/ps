#bronze 1


def mul(a, b):
    ans = 0
    for x in range(m):
            ans += A[a][x]*B[x][b]
    return ans


n, m = map(int, input().split())

A = [list(map(int, input().split())) for x in range(n)]

m, k = map(int, input().split())

B = [list(map(int, input().split())) for x in range(m)]

for x in range(n):
    for y in range(k):
        print(mul(x, y), end=' ')
    print()
