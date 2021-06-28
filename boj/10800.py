#gold 3

import sys
input = sys.stdin.readline

n = int(input())
box = []

for x in range(n):
    c, s = map(int, input().split())
    box.append((s, c, x))

box.sort()

ans = [0 for x in range(n)]
ps = [0 for x in range(n+1)]

temp = 0
idx = 0

#ans = 누적합 - 색 누적합
for x in range(n):
    while box[idx][0] < box[x][0]:
        ps[box[idx][1]] += box[idx][0]
        temp += box[idx][0]
        idx += 1

    ans[box[x][2]] = temp - ps[box[x][1]]

for x in range(n):
    print(ans[x])
