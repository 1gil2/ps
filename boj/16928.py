#silver 1

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    visit = [0 for x in range(101)]
    visit[1] = 1
    dq = deque()
    dq.append([1, 0])

    while dq:
        cur, cnt = dq.popleft()

        if cur == 100:
            return print(cnt)

        for i in range(1, 7):
            nxt = cur + i

            if nxt > 100:
                continue

            if nxt in ladder_check:
                nxt = ladder[nxt]
            elif nxt in snake_check:
                nxt = snake[nxt]

            if visit[nxt] == 0:
                visit[nxt] = 1
                dq.append([nxt, cnt + 1])


n, m = map(int, input().split())

ladder = {}
ladder_check = []
snake = {}
snake_check = []

for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
    ladder_check.append(x)

for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v
    snake_check.append(u)

bfs()
