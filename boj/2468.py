#silver 1

import sys

sys.setrecursionlimit(100000)


def dfs(x, y, h):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and table[nx][ny] > h:
            visit[nx][ny] = True
            dfs(nx, ny, h)


n = int(sys.stdin.readline())
table = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1

for x in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

M = 0
m = 101

for x in table:
    M = max(M, max(x))
    m = min(m, min(x))

for k in range(m, M):
    visit = [[False] * n for x in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if table[x][y] > k and visit[x][y] == 0:
                cnt += 1
                visit[x][y] = True
                dfs(x, y, k)
    ans = max(ans, cnt)

print(ans)
