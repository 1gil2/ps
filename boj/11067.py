#silver 1

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cafe = [(0, 0)]
    d = dict()

    for i in range(n):
        x, y = map(int, input().split())
        if x not in d:
            d[x] = []
        d[x].append(y)

    d2 = sorted(d.items())

    le = len(d2)
    for i in range(le):
        d2[i][1].sort()
        if cafe[-1][1] != d2[i][1][0]:
            d2[i][1].sort(reverse = True)
        le2 = len(d2[i][1])
        for j in range(le2):
            cafe.append((d2[i][0], d2[i][1][j]))

    m = list(map(int, input().split()))
    le3 = len(m)
    for i in range(1, le3):
        print(*cafe[m[i]])
