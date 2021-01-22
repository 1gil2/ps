#silver 1

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visit = [0 for x in range(100001)]

dq = deque()
dq.append([n, 0])
visit[n] = 1

while dq:
    A = dq.popleft()

    if A[0] == k:
        print(A[1])
        break

    if A[0] < 50001 and visit[A[0] * 2] == 0:
        dq.append([A[0] * 2, A[1] + 1])
        visit[2 * A[0]] = 1
    if A[0] > 0 and visit[A[0] - 1] == 0:
        dq.append([A[0] - 1, A[1] + 1])
        visit[A[0] - 1] = 1
    if A[0] + 1 <= 100000 and visit[A[0] + 1] == 0:
        dq.append([A[0] + 1, A[1] + 1])
        visit[A[0] + 1] = 1
