#gold 4

import sys
input = sys.stdin.readline

n = int(input())

blocks = []
for idx in range(1, n+1):
    area, height, weight = map(int, input().split())
    blocks.append((area, height, weight, idx))

blocks.sort()

#dp[x] x가 바닥일때 최대 높이
dp = [0 for x in range(n+1)]

for x in range(n):
    dp[x] = blocks[x][1]

    for y in range(x):
        if blocks[x][2] > blocks[y][2]:
            dp[x] = max(dp[x], dp[y] + blocks[x][1])

temp = 0
idx = 0
for i, x in enumerate(dp):
    if temp < x:
        temp = x
        idx = i

answer = []
while idx >= 0:
    if dp[idx] == temp:
        answer.append(blocks[idx][3])
        temp -= blocks[idx][1]
    idx -= 1

answer.reverse()

print(len(answer))
for x in answer:
    print(x)
