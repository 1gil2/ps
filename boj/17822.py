#gold 3

import sys
from collections import deque

input = sys.stdin.readline


# 원판돌리기
def rotate_table(x, d, k):
    if d == 1:
        k *= -1
    for i in range(1, n + 1):
        if i % x == 0:
            table[i].rotate(k)


# 원판작업하기
def work_table():
    s = []
    for y in range(m):
        for x in range(1, n + 1):
            if table[x][y] == 0:
                continue
            if table[x][y] == table[x - 1][y] or table[x][y] == table[x + 1][y]:
                s.append((x, y))

    for y in range(m):
        for x in range(1, n + 1):
            if table[x][y] == 0:
                continue
            if y == m - 1:
                if table[x][y] == table[x][y - 1] or table[x][0] == table[x][y]:
                    s.append((x, y))
            elif table[x][y] == table[x][y - 1] or table[x][y] == table[x][y + 1]:
                s.append((x, y))

    for x, y in s:
        table[x][y] = 0

    if len(s) == 0:
        su = 0
        cnt = 0
        for x in range(1, n + 1):
            for y in range(m):
                if table[x][y] == 0:
                    continue
                su += table[x][y]
                cnt += 1
        if su != 0 and cnt != 0:
            avg = su / cnt
            for x in range(1, n + 1):
                for y in range(m):
                    if table[x][y] == 0:
                        continue
                    if table[x][y] > avg:
                        table[x][y] -= 1
                    elif table[x][y] < avg:
                        table[x][y] += 1


n, m, t = map(int, input().split())
table = [[0 for x in range(m)]]
for x in range(n):
    dq = deque(map(int, input().split()))
    table.append(dq)
table.append([0 for x in range(m)])

for _ in range(t):
    x, d, k = map(int, input().split())
    # 원판돌리기
    rotate_table(x, d, k)

    # 원판작업하기
    work_table()

ans = 0
for x in range(1, n + 1):
    for y in range(m):
        ans += table[x][y]

print(ans)
