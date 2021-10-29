#gold 3

import sys
from collections import deque

input = sys.stdin.readline

d = (('N', -1, 0), ('S', 1, 0), ('E', 0, 1), ('W', 0, -1))


def bfs(sx1, sy1, sx2, sy2):
    visit = [[[[False for x in range(c)] for y in range(r)] for z in range(c)] for w in range(r)]
    visit[sx1][sy1][sx2][sy2] = True
    dq = deque()
    dq.append((0, '', sx1, sy1, sx2, sy2))

    while dq:
        cnt, st, x1, y1, x2, y2 = dq.popleft()

        if x1 == x2 and y1 == y2:
            print(cnt, st)
            return

        for s, dx, dy in d:
            x11 = x1 + dx
            y11 = y1 + dy
            x22 = x2 + dx
            y22 = y2 + dy

            if not 0 <= x11 < r:
                if x11 < 0:
                    x11 = r - 1
                else:
                    x11 = 0
            if not 0 <= y11 < c:
                if y11 < 0:
                    y11 = c - 1
                else:
                    y11 = 0
            if not 0 <= x22 < r:
                if x22 < 0:
                    x22 = r - 1
                else:
                    x22 = 0
            if not 0 <= y22 < c:
                if y22 < 0:
                    y22 = c - 1
                else:
                    y22 = 0

            if table[x11][y11] == 'X':
                x11 = x1
                y11 = y1
            if table[x22][y22] == 'X':
                x22 = x2
                y22 = y2

            if table[x11][y11] == 'G' or table[x22][y22] == 'G':
                continue

            if not visit[x11][y11][x22][y22]:
                visit[x11][y11][x22][y22] = True
                dq.append((cnt + 1, st + s, x11, y11, x22, y22))

    print('IMPOSSIBLE')
    return


t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    table = [list(input().rstrip()) for x in range(r)]

    flag = True
    for x in range(r):
        for y in range(c):
            if table[x][y] == 'P':
                table[x][y] = '.'
                if flag:
                    sx1, sy1 = x, y
                    flag = False
                else:
                    sx2, sy2 = x, y

    bfs(sx1, sy1, sx2, sy2)
