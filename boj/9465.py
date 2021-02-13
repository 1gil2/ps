#silver 2

T = int(input())

for x in range(T):
    a = [[], []]
    n = int(input())
    a[0].append(list(map(int, input().split())))
    a[1].append(list(map(int, input().split())))

    d = [[0], [a[0][0][0]], [a[1][0][0]]]

    for y in range(1, n):
        for z in range(3):
            if z == 0:
                d[0].append(max(d[0][y-1], d[1][y-1], d[2][y-1]))
            elif z == 1:
                d[1].append(max(d[0][y-1], d[2][y-1])+a[0][0][y])
            else:
                d[2].append(max(d[0][y-1], d[1][y-1])+a[1][0][y])

    print(max(d[0][n-1], d[1][n-1], d[2][n-1]))
