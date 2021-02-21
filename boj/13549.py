#gold 5

import sys

n, k = map(int, sys.stdin.readline().split())

visit = [0 for x in range(100001)]

Q = [[n, 0]]
visit[n] = 1

while len(Q) > 0:
    A = Q.pop(0)

    if A[0] == k:
        print(A[1])
        break

    if A[0] < 50001 and visit[A[0] * 2] == 0:
        Q.append([A[0] * 2, A[1]])
        visit[2 * A[0]] = 1
    if A[0] > 0 and visit[A[0] - 1] == 0:
        Q.append([A[0] - 1, A[1] + 1])
        visit[A[0] - 1] = 1
    if A[0] + 1 <= 100000 and visit[A[0] + 1] == 0:
        Q.append([A[0] + 1, A[1] + 1])
        visit[A[0] + 1] = 1
