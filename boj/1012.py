#silver 2

import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    table.remove([x, y])
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if [x + dx, y + dy] in table:
            dfs(x + dx, y + dy)


for x in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    table = []
    cnt = 0
    for i in range(k):
        table.append(list(map(int, sys.stdin.readline().split())))
    while True:
        dfs(table[0][0], table[0][1])
        cnt += 1
        if len(table) == 0:
            break
    print(cnt)
