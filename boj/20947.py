#gold 4
#pypy3

import sys
input = sys.stdin.readline


def solve(x, y):
    # 위
    tx = x
    while tx > 0:
        tx -= 1
        if table[tx][y] == '.':
            table[tx][y] = 'N'
        elif table[tx][y] == 'N':
            continue
        else:
            break
    # 아래
    tx = x
    while tx < n - 1:
        tx += 1
        if table[tx][y] == '.':
            table[tx][y] = 'N'
        elif table[tx][y] == 'N':
            continue
        else:
            break
    # 왼
    ty = y
    while ty > 0:
        ty -= 1
        if table[x][ty] == '.':
            table[x][ty] = 'N'
        elif table[x][ty] == 'N':
            continue
        else:
            break
    # 오
    ty = y
    while ty < n - 1:
        ty += 1
        if table[x][ty] == '.':
            table[x][ty] = 'N'
        elif table[x][ty] == 'N':
            continue
        else:
            break


n = int(input())
table = []
for x in range(n):
    temp = input().strip()
    tt = []
    for s in temp:
        tt.append(s)
    table.append(tt)

for x in range(n):
    for y in range(n):
        if table[x][y] == 'O':
            solve(x, y)

for x in range(n):
    for y in range(n):
        if table[x][y] == '.':
            table[x][y] = 'B'
        if table[x][y] == 'N':
            table[x][y] = '.'

for t in table:
    print(''.join(t))
