#platinum 3

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

area = list(map(int, input().split())) + [0]

stack = []

cnt = 0
water = 0

for idx in range(n + 1):
    left = idx
    pool = 0
    flag = True

    while stack and stack[-1][2] >= area[idx]:
        left, right, height, pool2 = stack.pop()

        dh = height - area[idx]

        if dh == 0:
            pool += pool2
        else:
            cnt -= pool2

            if flag:
                cnt += 1
                flag = False
                pool = 1

        if cnt == k:
            print(water)
            sys.exit()

        water += dh * (right - left)

    stack.append((left, idx + 1, area[idx], pool))

print(-1)
