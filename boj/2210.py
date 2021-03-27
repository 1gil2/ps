#silver 2

import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, depth):
    global ans
    if depth == 6:
        S.add(ans)
        return

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        if 0 <= x1 < 5 and 0 <= y1 < 5:
            ans += str(table[x1][y1])
            dfs(x1, y1, depth + 1)
            ans = ans[:-1]


table = [list(map(int, input().split())) for x in range(5)]

S = set()
ans = ''

for i in range(5):
    for j in range(5):
        ans += str(table[i][j])
        dfs(i, j, 1)
        ans = ''

print(len(S))
