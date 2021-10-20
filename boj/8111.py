#platinum 5

import sys
from collections import deque

input = sys.stdin.readline


def bfs(n):
    if n == 1:
        print(1)
        return

    q = deque()
    q.append((1, '1', 1))
    visit = [False for x in range(n)]
    visit[1] = True

    while q:
        m, st, le = q.popleft()

        if le > 100:
            continue
        if m == 0:
            print(st)
            return

        m1 = (m * 10) % n
        m2 = (m * 10 + 1) % n

        if not visit[m1]:
            visit[m1] = True
            q.append((m1, st + '0', le + 1))
        if not visit[m2]:
            visit[m2] = True
            q.append((m2, st + '1', le + 1))

    print('BRAK')
    return


t = int(input())
for _ in range(t):
    num = int(input())
    bfs(num)
