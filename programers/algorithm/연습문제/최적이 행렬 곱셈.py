#level 4

import sys


def solution(matrix_sizes):
    lm = len(matrix_sizes)
    table = [[sys.maxsize for y in range(lm)] for x in range(lm)]

    for x in range(lm):
        table[x][x] = 0

    for gap in range(1, lm):
        for x in range(lm):
            y = x + gap
            if y >= lm:
                break
            for k in range(x, y):
                temp = table[x][k] + table[k + 1][y] + matrix_sizes[x][0] * matrix_sizes[k][1] * matrix_sizes[y][1]
                if table[x][y] > temp:
                    table[x][y] = temp

    return table[0][-1]
