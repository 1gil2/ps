#gold 4

import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))

ans = 0
for i, height in enumerate(buildings):
    cnt = 0

    temp = sys.maxsize
    for i2 in range(i - 1, -1, -1):
        d = (buildings[i2] - height) / (i2 - i)

        if temp > d:
            temp = d
            cnt += 1

    temp = -sys.maxsize
    for i2 in range(i + 1, n):
        d = (buildings[i2] - height) / (i2 - i)

        if temp < d:
            temp = d
            cnt += 1

    ans = max(ans, cnt)

print(ans)
