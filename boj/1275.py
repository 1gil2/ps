#gold 1

import sys
from math import log, ceil

input = sys.stdin.readline


def init():
    for x in range(n):
        tree[x + size] = arr[x]
    for x in range(size - 1, 0, -1):
        tree[x] = tree[2 * x] + tree[2 * x + 1]


def modify(idx, val):
    idx += size - 1
    tree[idx] = val
    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


def total(root, left, right, start, end):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[root]

    mid = (left + right) // 2
    return total(root * 2, left, mid, start, end) + total(root * 2 + 1, mid + 1, right, start, end)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
size = 2 ** ceil(log(n, 2))
tree = [0 for x in range(2 * size)]
init()

for _ in range(m):
    x, y, a, b = map(int, input().split())

    if x < y:
        print(total(1, 0, size - 1, x - 1, y - 1))
    else:
        print(total(1, 0, size - 1, y - 1, x - 1))

    modify(a, b)
