#gold 4

import sys
from copy import deepcopy

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def turn(L):
    temp = deepcopy(ice)
    for x in range(0, le, L):
        for y in range(0, le, L):
            for i in range(L):
                for j in range(L):
                    ice[x + i][y + j] = temp[x + L - j - 1][y + i]


def melt():
    temp = deepcopy(ice)
    for x in range(le):
        for y in range(le):
            cnt = 0
            for i in range(4):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < le and 0 <= y1 < le and temp[x1][y1]:
                    cnt += 1
            if cnt < 3 and ice[x][y] > 0:
                ice[x][y] -= 1


def dfs(x, y):
    cnt = 1
    ice[x][y] = 0
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < le and 0 <= y1 < le and ice[x1][y1]:
            cnt += dfs(x1, y1)

    return cnt


n, q = map(int, input().split())
le = 2 ** n

ice = []
for x in range(le):
    ice.append(list(map(int, input().split())))

LL = list(map(int, input().split()))

for L in LL:
    turn(2 ** L)
    melt()

total = 0
ans = 0

for x in range(le):
    total += sum(ice[x])

for x in range(le):
    for y in range(le):
        if ice[x][y] > 0:
            ans = max(ans, dfs(x, y))

print(total)
print(ans)
