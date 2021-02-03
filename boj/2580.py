#gold 4
#pypy3

import sys
input = sys.stdin.readline


def change(a, b):
    return (a//3) * 3 + b//3


def back(cnt):
    if cnt == 81:
        for x in range(9):
            for y in range(9):
                print(table[x][y], end=' ')
            print()
        sys.exit(0)
        return

    dy = cnt//9
    dx = cnt%9

    if table[dy][dx]:
        back(cnt+1)
    else:
        for k in range(1, 10):
            if col[dx][k] == 0 and row[dy][k] == 0 and squre[change(dy, dx)][k] == 0:
                table[dy][dx] = k
                col[dx][k] = 1
                row[dy][k] = 1
                squre[change(dy, dx)][k] = 1
                back(cnt+1)
                table[dy][dx] = 0
                col[dx][k] = 0
                row[dy][k] = 0
                squre[change(dy, dx)][k] = 0


table = [list(map(int, input().split())) for x in range(9)]
row = [[0 for y in range(10)] for x in range(9)]
col = [[0 for y in range(10)] for x in range(9)]
squre = [[0 for y in range(10)] for x in range(9)]

for y in range(9):
    for x in range(9):
        if table[x][y]:
            row[x][table[x][y]] = 1
            col[y][table[x][y]] = 1
            squre[change(x, y)][table[x][y]] = 1

back(0)
