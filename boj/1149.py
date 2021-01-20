#silver 1

n = int(input())
a = []

for x in range(n):
    a.append(list(map(int, input().split())))

d = [[], [], []]

for x in range(3):
    d[x].append(int(a[0][x]))
for x in range(1, n):
    for y in range(3):
        if y == 0:
            d[0].append(min(d[1][x-1], d[2][x-1])+a[x][y])
        elif y == 1:
            d[1].append(min(d[0][x-1], d[2][x-1])+a[x][y])
        else:
            d[2].append(min(d[1][x-1], d[0][x-1])+a[x][y])

print(min(d[0][n-1], d[1][n-1], d[2][n-1]))
