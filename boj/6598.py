#gold 2

import math

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    money = dict()
    for x in range(n):
        money[input()] = x

    table = [[0 for x in range(n)] for y in range(n)]

    m = int(input())
    for x in range(m):
        a, b, c = input().split()
        table[money[a]][money[c]] = -math.log(float(b))

    e = input()

    for x in range(n):
        for y in range(n):
            for z in range(n):
                table[x][y] = min(table[x][y], table[x][z]+table[z][y])

    for x in range(n):
        if table[x][x] < 0:
            print("Case %d: Yes" %cnt)
            break
    else:
        print("Case %d: No" %cnt)
