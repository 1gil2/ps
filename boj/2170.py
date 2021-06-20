#gold 5

import sys
input = sys.stdin.readline

n = int(input())

lines = []
for x in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()
left = lines[0][0]
right = lines[0][1]

ans = 0

for i, line in enumerate(lines):
    if i == 0:
        continue

    if right > line[0]:
        if right > line[1]:
            continue
        else:
            right = line[1]
    else:
        ans += right - left
        left = line[0]
        right = line[1]

ans += right - left
print(ans)
