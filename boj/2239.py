#gold 4

import sys
input = sys.stdin.readline


def dfs(idx):
    if idx == 81:
        for t in table:
            print(''.join(map(str, t)))
        sys.exit()
        return

    x = idx//9
    y = idx%9

    if table[x][y]:
        dfs(idx+1)
        return

    for i in range(1, 10):
        if not garo[x][i] and not sero[y][i] and not nemo[(x//3)*3 + y//3][i]:
            garo[x][i] = 1
            sero[y][i] = 1
            nemo[(x//3)*3 + y//3][i] = 1
            table[x][y] = i
            dfs(idx+1)
            garo[x][i] = 0
            sero[y][i] = 0
            nemo[(x//3)*3 + y//3][i] = 0
            table[x][y] = 0


table = [list(map(int, input().rstrip())) for x in range(9)]

garo = [[0 for x in range(10)] for y in range(9)]
sero = [[0 for x in range(10)] for y in range(9)]
nemo = [[0 for x in range(10)] for y in range(9)]

for x in range(9):
    for y in range(9):
        if table[x][y]:
            garo[x][table[x][y]] = 1
            sero[y][table[x][y]] = 1
            nemo[(x//3)*3 + y//3][table[x][y]] = 1

dfs(0)
