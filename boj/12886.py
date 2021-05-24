#gold 5

import sys
from collections import deque
input = sys.stdin.readline


def solve(a, b, c):
    total = a + b + c
    temp = total // 3
    if total % 3 != 0:
        return print(0)

    visit = [[0 for x in range(total + 1)] for y in range(total + 1)]
    dq = deque()
    dq.append((a, b))
    visit[a][b] = 1

    while dq:
        x, y = dq.popleft()
        z = total - x - y

        if x == y == z:
            return print(1)

        for i, j in ((x, y), (y, z), (z, x)):
            if i < j:
                j -= i
                i += i
            elif i > j:
                i -= j
                j += j
            else:
                continue
            k = total - i - j

            m = min(i, j, k)
            M = max(i, j, k)
            if not visit[m][M]:
                dq.append((m, M))
                visit[m][M] = 1

    return print(0)


a, b, c = map(int, input().split())
solve(a, b, c)
