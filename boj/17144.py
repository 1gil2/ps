#gold 5

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def myprint(table):
    for x in range(r):
        for y in range(c):
            print(table[x][y], end=' ')
        print()


def dust(table):
    temp = [[0 for y in range(c)] for x in range(r)]
    for x in range(r):
        for y in range(c):
            if table[x][y] > 0:
                a = table[x][y] // 5
                if x == 0 and y == 0:
                    temp[x][y] += table[x][y] - a - a
                    temp[x + 1][y] += a
                    temp[x][y + 1] += a
                elif x == r - 1 and y == 0:
                    temp[x][y] += table[x][y] - a - a
                    temp[x - 1][y] += a
                    temp[x][y + 1] += a
                elif x == 0 and y == c - 1:
                    temp[x][y] += table[x][y] - a - a
                    temp[x + 1][y] += a
                    temp[x][y - 1] += a
                elif x == r - 1 and y == c - 1:
                    temp[x][y] += table[x][y] - a - a
                    temp[x - 1][y] += a
                    temp[x][y - 1] += a
                elif x == 0:
                    temp[x][y] += table[x][y] - a - a - a
                    temp[x + 1][y] += a
                    temp[x][y + 1] += a
                    temp[x][y - 1] += a
                elif y == c - 1:
                    temp[x][y] += table[x][y] - a - a - a
                    temp[x + 1][y] += a
                    temp[x][y - 1] += a
                    temp[x - 1][y] += a
                elif x == r - 1:
                    temp[x][y] += table[x][y] - a - a - a
                    temp[x - 1][y] += a
                    temp[x][y + 1] += a
                    temp[x][y - 1] += a
                elif y == 0:
                    if x == cleaner[0] - 1:
                        temp[x][y] += table[x][y] - a - a
                        temp[x - 1][y] += a
                        temp[x][y + 1] += a
                    elif x == cleaner[1] + 1:
                        temp[x][y] += table[x][y] - a - a
                        temp[x + 1][y] += a
                        temp[x][y + 1] += a
                    else:
                        temp[x][y] += table[x][y] - a - a - a
                        temp[x + 1][y] += a
                        temp[x][y + 1] += a
                        temp[x - 1][y] += a
                elif y == 1 and x == cleaner[0]:
                    temp[x][y] += table[x][y] - a - a - a
                    temp[x + 1][y] += a
                    temp[x][y + 1] += a
                    temp[x - 1][y] += a
                elif y == 1 and x == cleaner[1]:
                    temp[x][y] += table[x][y] - a - a - a
                    temp[x + 1][y] += a
                    temp[x][y + 1] += a
                    temp[x - 1][y] += a
                else:
                    temp[x][y] += table[x][y] - a - a - a - a
                    temp[x + 1][y] += a
                    temp[x][y + 1] += a
                    temp[x - 1][y] += a
                    temp[x][y - 1] += a
    temp[cleaner[0]][0] = -1
    temp[cleaner[1]][0] = -1
    return temp


def air():
    for x in range(cleaner[0] - 1, -1, -1):
        table[x + 1][0] = table[x][0]
    for x in range(1, c):
        table[0][x - 1] = table[0][x]
    for x in range(1, cleaner[0] + 1):
        table[x - 1][-1] = table[x][-1]
    for x in range(c - 2, 0, -1):
        table[cleaner[0]][x + 1] = table[cleaner[0]][x]
    table[cleaner[0]][1] = 0
    table[cleaner[0]][0] = -1

    for x in range(cleaner[1] + 1, r):
        table[x - 1][0] = table[x][0]
    for x in range(1, c):
        table[-1][x - 1] = table[-1][x]
    for x in range(r - 2, cleaner[1] - 1, -1):
        table[x + 1][-1] = table[x][-1]
    for x in range(c - 2, 0, -1):
        table[cleaner[1]][x + 1] = table[cleaner[1]][x]
    table[cleaner[1]][1] = 0
    table[cleaner[1]][0] = -1


r, c, t = map(int, input().split())
table = [list(map(int, input().split())) for x in range(r)]

for x in range(r):
    if table[x][0] == -1:
        cleaner = [x, x + 1]
        break

for x in range(t):
    table = dust(table)
    air()

ans = 2
for x in range(r):
    ans += sum(table[x])

print(ans)
