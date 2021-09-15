#platinum 5

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start):
    sx = start[0]
    sy = start[1]

    visit = [[-1 for y in range(w + 2)] for x in range(h + 2)]
    visit[sx][sy] = 0
    dq = deque()
    dq.append((sx, sy))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < h + 2 and 0 <= y1 < w + 2:
                if visit[x1][y1] != -1:
                    continue

                if table[x1][y1] == '*':
                    continue

                if table[x1][y1] == '.':
                    visit[x1][y1] = visit[x][y]
                    dq.appendleft((x1, y1))
                elif table[x1][y1] == '#':
                    visit[x1][y1] = visit[x][y] + 1
                    dq.append((x1, y1))

    return visit


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())

    table = []
    table.append(['.' for x in range(w + 2)])
    for x in range(h):
        table.append(list('.' + input().rstrip() + '.'))
    table.append(['.' for x in range(w + 2)])

    people = []
    for x in range(h + 2):
        for y in range(w + 2):
            if table[x][y] == '$':
                people.append((x, y))
                table[x][y] = '.'

    p1 = people[0]
    p2 = people[1]
    visit1 = bfs(p1)
    visit2 = bfs(p2)
    visit3 = bfs((0, 0))

    ans = sys.maxsize
    for x in range(h + 2):
        for y in range(w + 2):
            if table[x][y] == '*':
                continue

            if visit1[x][y] == -1 or visit2[x][y] == -1 or visit3[x][y] == -1:
                continue

            temp = visit1[x][y] + visit2[x][y] + visit3[x][y]
            if table[x][y] == '#':
                temp -= 2

            ans = min(ans, temp)

    print(ans)
