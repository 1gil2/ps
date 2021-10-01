#platinum 5
#pypy3

import sys
input = sys.stdin.readline


def update(x, y, val):
    x1 = x + size
    y1 = y + size
    tree[x1][y1] = val

    while y1 > 1:
        y1 //= 2
        tree[x1][y1] = tree[x1][y1 * 2] + tree[x1][y1 * 2 + 1]

    while x1 > 1:
        y1 = y + size
        x1 //= 2
        tree[x1][y1] = tree[x1 * 2][y1] + tree[x1 * 2 + 1][y1]
        while y1 > 1:
            y1 //= 2
            tree[x1][y1] = tree[x1][y1 * 2] + tree[x1][y1 * 2 + 1]


def query(x1, y1, x2, y2):
    ret = 0
    x1 += size
    x2 += size

    while x1 <= x2:
        if x1 % 2 == 1:
            ret += query2(x1, y1, y2)
            x1 += 1
        if x2 % 2 == 0:
            ret += query2(x2, y1, y2)
            x2 -= 1

        x1 >>= 1
        x2 >>= 1

    return ret


def query2(x, y1, y2):
    ret = 0
    y1 += size
    y2 += size

    while y1 <= y2:
        if y1 % 2 == 1:
            ret += tree[x][y1]
            y1 += 1
        if y2 % 2 == 0:
            ret += tree[x][y2]
            y2 -= 1

        y1 >>= 1
        y2 >>= 1

    return ret


n, m = map(int, input().split())

size = 1
while size < n:
    size <<= 1

tree = [[0 for y in range(2 * size)] for x in range(2 * size)]

arr = [list(map(int, input().split())) for x in range(n)]
for x in range(n):
    for y in range(n):
        update(x, y, arr[x][y])

for _ in range(m):
    cmds = list(map(int, input().split()))

    if cmds[0]:
        x1, y1, x2, y2 = cmds[1:]

        print(query(x1 - 1, y1 - 1, x2 - 1, y2 - 1))

    else:
        x, y, val = cmds[1:]
        update(x - 1, y - 1, val)
