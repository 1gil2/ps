#gold 5

import sys
input = sys.stdin.readline


def calc(a1, a2, a3):
    return a1[0] * a2[1] + a2[0] * a3[1] + a3[0] * a1[1] - a2[0] * a1[1] - a3[0] * a2[1] - a1[0] * a3[1]


n = int(input())
xy = []
ans = 0
for _ in range(n):
    xy.append(list(map(int, input().split())))

for i in range(n - 2):
    ans += calc(xy[0], xy[i + 1], xy[i + 2]) / 2

print(round(abs(ans), 1))
