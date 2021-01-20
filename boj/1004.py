#silver 3

def inner1(a, b, r):
    if (a - x1) ** 2 + (b - y1) ** 2 < r ** 2:
        return 1
    return 0

def inner2(a, b, r):
    if (a - x2) ** 2 + (b - y2) ** 2 < r ** 2:
        return 1
    return 0

for x in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for y in range(n):
        c1, c2, r = map(int, input().split())
        cnt += (inner1(c1, c2, r) + inner2(c1, c2, r)) % 2
    print(cnt)