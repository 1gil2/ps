#gold 4

import sys
from collections import deque
input = sys.stdin.readline


def change(b):
    if b == 0:
        return b

    b *= 2
    if b > 99999:
        return b

    numlist = [x for x in str(b)]
    for i, x in enumerate(numlist):
        if x != '0':
            numlist[i] = str(int(numlist[i]) - 1)
            break

    return int(''.join(numlist))


n, t, g = map(int, input().split())

dq = deque()
dq.append((0, n))
visit = [0 for x in range(100000)]
visit[n] = 1
flag = False

while dq:
    cnt, num = dq.popleft()

    if cnt > t:
        continue
    if num == g:
        ans = cnt
        flag = True
        break

    A = num + 1
    if A < 100000 and visit[A] == 0:
        visit[A] = 1
        dq.append((cnt + 1, A))

    B = change(num)
    if B < 100000 and visit[B] == 0:
        visit[B] = 1
        dq.append((cnt + 1, B))

if flag:
    print(ans)
else:
    print("ANG")
