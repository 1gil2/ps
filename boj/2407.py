#silver 2

n, m = map(int, input().split())

C = [[0 for x in range(n+1)] for x in range(n+1)]

for x in range(n+1):
    C[x][0] = 1
    C[x][x] = 1

for x in range(2, n+1):
    for y in range(1, x+1):
        if y == x:
            continue
        else:
            C[x][y] = C[x-1][y-1]+C[x-1][y]

print(C[n][m])
