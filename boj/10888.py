#gold 2

import sys
input = sys.stdin.readline


def find(idx):
    if idx == parent[idx]:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a > b:
        a, b = b, a

    parent[b] = a


def calc(num):
    return num * (num - 1) // 2


def calc2(num):
    return num * (num + 1) * (num - 1) // 6


n = int(input())

parent = [x for x in range(n + 1)]
have = [1 for x in range(n + 1)]

ans1 = 0
ans2 = 0

for _ in range(n - 1):
    i = int(input())

    x = find(i)
    y = find(i + 1)

    hx = have[x]
    hy = have[y]

    ans1 += calc(hx + hy) - calc(hx) - calc(hy)
    ans2 += calc2(hx + hy) - calc2(hx) - calc2(hy)

    union(x, y)
    have[x] += have[y]

    print(ans1, ans2)
