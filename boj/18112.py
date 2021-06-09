#gold 5

import sys
from collections import deque

input = sys.stdin.readline


def bi_le(x):
    le = 0

    while x:
        x //= 2
        le += 1

    return le


def calc(st):
    ret = 0
    le = len(st)
    for x in range(le):
        ret += int(st[-x - 1]) * int(2 ** x)

    return ret


n = calc(input().rstrip())
m = calc(input().rstrip())

dq = deque()
dq.append((n, 0))

visit = [0 for x in range(2 ** 11)]
visit[n] = 1

while dq:
    num, cnt = dq.popleft()

    if num == m:
        print(cnt)
        break

    if num + 1 < 2 ** 10 and visit[num + 1] == 0:
        visit[num + 1] = 1
        dq.append((num + 1, cnt + 1))

    if num > 0 and visit[num - 1] == 0:
        visit[num - 1] = 1
        dq.append((num - 1, cnt + 1))

    if 0 < num < 2 ** 10:
        le = bi_le(num)
        for x in range(le - 1):
            temp = num ^ (1 << x)

            if visit[temp] == 0:
                visit[temp] = 1
                dq.append((temp, cnt + 1))
