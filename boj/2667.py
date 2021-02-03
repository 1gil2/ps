#silver 1

import sys


def dfs(a, b):
    global cnt2
    table[a][b] = '0'
    cnt2 += 1
    for i in range(4):
        dx = xd[i]
        dy = yd[i]
        if a+dx >= n or a+dx < 0 or b+dy >= n or b+dy < 0:
            continue
        if table[a+dx][b+dy] == '1':
            dfs(a+dx, b+dy)


xd = [0, 0, 1, -1]
yd = [1, -1, 0, 0]

n = int(input())
table = []
for x in range(n):
    table.append(list(sys.stdin.readline()))

cnt = 0
cnt2 = 0
home = []
for x in range(n):
    for y in range(n):
        if table[x][y] == '1':
            cnt2 = 0
            dfs(x, y)
            cnt += 1
            home.append(cnt2)

print(cnt)
home.sort()
for x in home:
    print(x)
