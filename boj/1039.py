#gold 3


import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def bfs():
    global dq
    s = set()
    temp_dq = deque()
    res = 0
    while dq:
        a = dq.popleft()
        num = list(str(a))
        for i, j in combi:
            temp = num[:]
            temp[i], temp[j] = temp[j], temp[i]
            if temp[0] == '0':
                continue

            new_n = int("".join(temp))
            if new_n not in s:
                res = max(res, new_n)
                s.add(new_n)
                temp_dq.append(new_n)

    dq = temp_dq
    return res


n, k = map(int, input().split())

combi = list(combinations([x for x in range(len(str(n)))] , 2))

dq = deque()
dq.append(n)
ans = 0

while k:
    ans = bfs()
    k -= 1

if ans:
    print(ans)
else:
    print(-1)
