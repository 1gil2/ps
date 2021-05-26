#gold 5
#pypy3

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    res = []
    res.append((i, j))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < n and visit[x1][y1] == 0:
                if l <= abs(table[x][y] - table[x1][y1]) <= r:
                    visit[x1][y1] = 1
                    dq.append((x1, y1))
                    res.append((x1, y1))

    return res


n, l, r = map(int, input().split())
table = [list(map(int, input().split())) for x in range(n)]

cnt = 0

while True:
    visit = [[0 for x in range(n)] for y in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                conn = bfs(i, j)
                if len(conn) > 1:
                    flag = True
                    people = 0
                    for x, y in conn:
                        people += table[x][y]

                    people //= len(conn)

                    for x, y in conn:
                        table[x][y] = people

    if flag == False:
        break
    cnt += 1

print(cnt)
