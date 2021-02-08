#silver 2

from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(x, y):
    table[x][y] = 0
    Q = [[x, y]]
    dq = deque(Q)

    while dq:
        a = dq[0][0]
        b = dq[0][1]

        dq.popleft()

        for i in range(8):
            x1 = a + dx[i]
            y1 = b + dy[i]

            if 0 <= x1 < h and 0 <= y1 < w and table[x1][y1] == 1:
                table[x1][y1] = 0
                dq.append([x1, y1])


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    table = [list(map(int, input().split())) for x in range(h)]

    cnt = 0

    for x in range(h):
        for y in range(w):
            if table[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)
