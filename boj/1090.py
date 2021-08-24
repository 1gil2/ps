#platinum 5

import sys
input = sys.stdin.readline

n = int(input())

points = []
xs = []
ys = []

ans = [sys.maxsize for x in range(n)]

for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    points.append((x, y))

xs.sort()
ys.sort()
points.sort()

for x in xs:
    for y in ys:

        dist = []
        for point in points:
            dist.append(abs(x - point[0]) + abs(y - point[1]))

        dist.sort()

        temp = 0
        for k in range(n):
            temp += dist[k]
            ans[k] = min(ans[k], temp)

for a in ans:
    print(a, end = ' ')
