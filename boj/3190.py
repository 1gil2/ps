#gold 5

import sys
from collections import deque
input = sys.stdin.readline


# 방향 전환
def turn(v, cmd):
    if v == 0:
        if cmd == 'L':
            return 2
        if cmd == 'D':
            return 3
    if v == 1:
        if cmd == 'L':
            return 3
        if cmd == 'D':
            return 2
    if v == 2:
        if cmd == 'L':
            return 1
        if cmd == 'D':
            return 0
    if v == 3:
        if cmd == 'L':
            return 0
        if cmd == 'D':
            return 1


# 뱀의 머리가 갈 다음 칸
def next(x, y, v):
    if vec == 0:
        return x - 1, y
    if vec == 1:
        return x + 1, y
    if vec == 2:
        return x, y - 1
    if vec == 3:
        return x, y + 1


N = int(input())
K = int(input())
table = [[0 for y in range(N + 1)] for x in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    table[a][b] = 1

L = int(input())
time_move = deque()
vec_move = deque()
for _ in range(L):
    x, c = map(str, input().split())
    time_move.append(int(x))
    vec_move.append(c)

snake = deque()
snake.append((1, 1))
# 머리 방향 : 상 0 하 1 좌 2 우 3
vec = 3
time = 0
x = 1
y = 1

while True:
    time += 1

    dx, dy = next(x, y, vec)

    # 자신의 몸에 부딪힘
    if (dx, dy) in snake:
        break
    # 벽에 부딪힘
    if dx < 1 or dx > N or dy < 1 or dy > N:
        break

    x = dx
    y = dy

    # 사과를 먹으면 머리만 늘어남
    if table[dx][dy] == 1:
        table[dx][dy] = 0
        snake.append((dx, dy))
    else:
        snake.append((dx, dy))
        snake.popleft()

    # 이동 커맨드 체크
    if time in time_move:
        time_move.popleft()
        vec = turn(vec, vec_move.popleft())

print(time)
