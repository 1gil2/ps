#gold 2

from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 8)


def left(table):
    for i in range(n):
        p = 0
        temp = 0
        for q in range(n):
            if table[i][q] == 0:
                continue
            if temp == 0:
                temp = table[i][q]
            else:
                if temp == table[i][q]:
                    table[i][p] = 2 * temp
                    p = p + 1
                    temp = 0
                else:
                    table[i][p] = temp
                    p = p + 1
                    temp = table[i][q]

            table[i][q] = 0

        if temp != 0:
            table[i][p] = temp

    return table


def right(table):
    for i in range(n):
        p = n - 1
        temp = 0
        for q in range(n - 1, -1, -1):
            if table[i][q] == 0:
                continue
            if temp == 0:
                temp = table[i][q]
            else:
                if temp == table[i][q]:
                    table[i][p] = 2 * temp
                    p = p - 1
                    temp = 0
                else:
                    table[i][p] = temp
                    p = p - 1
                    temp = table[i][q]

            table[i][q] = 0

        if temp != 0:
            table[i][p] = temp

    return table


def up(table):
    for i in range(n):
        p = 0
        temp = 0
        for q in range(n):
            if table[q][i] == 0:
                continue
            if temp == 0:
                temp = table[q][i]
            else:
                if temp == table[q][i]:
                    table[p][i] = 2 * temp
                    p = p + 1
                    temp = 0
                else:
                    table[p][i] = temp
                    p = p + 1
                    temp = table[q][i]

            table[q][i] = 0

        if temp != 0:
            table[p][i] = temp

    return table


def down(table):
    for i in range(n):
        p = n - 1
        temp = 0
        for q in range(n - 1, -1, -1):
            if table[q][i] == 0:
                continue
            if temp == 0:
                temp = table[q][i]
            else:
                if temp == table[q][i]:
                    table[p][i] = 2 * temp
                    p = p - 1
                    temp = 0
                else:
                    table[p][i] = temp
                    p = p - 1
                    temp = table[q][i]

            table[q][i] = 0

        if temp != 0:
            table[p][i] = temp

    return table


def max_value(table):
    global M

    for x in range(n):
        for y in range(n):
            if M < table[x][y]:
                M = table[x][y]


def dfs(table, cnt):
    if cnt == 5:
        max_value(table)
        return

    dfs(left(deepcopy(table)), cnt + 1)
    dfs(right(deepcopy(table)), cnt + 1)
    dfs(up(deepcopy(table)), cnt + 1)
    dfs(down(deepcopy(table)), cnt + 1)


n = int(input())
table = [list(map(int, input().split())) for x in range(n)]
M = 0

dfs(table, 0)
print(M)
