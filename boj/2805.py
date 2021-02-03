#silver 3
#pypy3

import sys
input = sys.stdin.readline


def cut(x):
    k = 0
    for i in range(n):
        k += max(wood[i] - x, 0)

    return k >= m


n, m = map(int, input().split())
wood = list(map(int, input().split()))

low = 0
height = max(wood)

while low <= height:
    mid = (low + height)//2

    if cut(mid):
        low = mid + 1
    else:
        height = mid -1

print(low - 1)
