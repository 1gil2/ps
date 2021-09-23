#level 2


from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visit = [[0 for y in range(m)] for x in range(n)]
    dq = deque()
    dq.append([0, 0, 1])

    while dq:
        x, y, cnt = dq.popleft()

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]

            if 0 <= x1 < n and 0 <= y1 < m:
                if maps[x1][y1] == 0:
                    continue
                if visit[x1][y1] != 0:
                    continue
                visit[x1][y1] = 1
                dq.append([x1, y1, cnt + 1])

    return -1
