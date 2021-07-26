#gold 2

import sys
from itertools import combinations
from math import sqrt

input = sys.stdin.readline


def calc(com):
    x = 0
    y = 0
    for c in com:
        x += c[0]
        y += c[1]

    return x, y


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


t = int(input())
for _ in range(t):
    n = int(input())

    dots = []
    sum_x = 0
    sum_y = 0
    ans = sys.maxsize

    for i in range(n):
        x, y = map(int, input().split())
        sum_x += x
        sum_y += y
        dots.append((x, y))

    combi = combinations(dots, n // 2)

    for com in combi:
        x1, y1 = calc(com)
        x2 = sum_x - x1
        y2 = sum_y - y1
        ans = min(ans, dist(x1, y1, x2, y2))

    print(ans)
