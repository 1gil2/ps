#bronze 2

n = int(input())

table = [[' ' for x in range(n)] for y in range(2*n)]

for x in range(n):
    for y in range(2*n):
        if (x+y) % 2 == 0:
            table[y][x] = '*'

for x in range(2*n):
    for y in range(n):
        print(table[x][y], end='')
    print()
