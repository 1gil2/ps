#gold 4

import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, sx, sy, cnt, color):
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        if x1 == sx and y1 == sy and cnt > 3:
            print('Yes')
            sys.exit()

        if 0 <= x1 < n and 0 <= y1 < m:
            if not visit[x1][y1] and table[x1][y1] == color:
                visit[x1][y1] = True
                dfs(x1, y1, sx, sy, cnt + 1, color)
                visit[x1][y1] = False


n, m = map(int, input().split())
table = [list(input().rstrip()) for x in range(n)]
visit = [[False for y in range(m)] for x in range(n)]

for x in range(n):
    for y in range(m):
        if not visit[x][y]:
            visit[x][y] = True
            dfs(x, y, x, y, 1, table[x][y])

print('No')
