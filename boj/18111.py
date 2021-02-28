#silver 3

import sys

n, m, b = map(int, sys.stdin.readline().split())

table = []

for x in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

Ma = 0
ma = 123456789

for x in range(n):
    for y in range(m):
        ma = min(table[x][y], ma)
        Ma = max(table[x][y], Ma)

time = 123456789
height = 0

for h in range(ma, Ma + 1):
    build = 0
    remove = 0

    for x in range(n):
        for y in range(m):
            temp = h - table[x][y]

            if temp < 0:
                remove += temp * (-1)
            else:
                build += temp

    if build <= remove + b:
        temp2 = build + 2 * remove

        if time > temp2:
            time = temp2
            height = h

        if time == temp2:
            if height < h:
                height = h

print(time, height)
