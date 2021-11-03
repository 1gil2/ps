#gold 4

import sys

input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())

cube = [0 for x in range(20)]
for _ in range(n):
    a, b = map(int, input().split())
    cube[a] = b

past = 0
cnt = 0

for x in range(19, -1, -1):
    past *= 8

    m = int(2 ** x)

    temp = min(cube[x], (l // m) * (w // m) * (h // m) - past)

    past += temp
    cnt += temp

volumn = l * w * h

if past == volumn:
    print(cnt)
else:
    print(-1)
