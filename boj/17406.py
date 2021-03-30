# gold 4

import sys
input = sys.stdin.readline


def turn(r, c, s):
    for d in range(1, s + 1):
        temp = A[r - d][c - d]
        for i in range(r - d, r + d):
            A[i][c - d] = A[i + 1][c - d]
        for j in range(c - d, c + d):
            A[r + d][j] = A[r + d][j + 1]
        for i in range(r + d, r - d, -1):
            A[i][c + d] = A[i - 1][c + d]
        for j in range(c + d, c - d, -1):
            A[r - d][j] = A[r - d][j - 1]
        A[r - d][c - d + 1] = temp


def turn2(r, c, s):
    for d in range(1, s + 1):
        temp = A[r - d][c - d]
        for j in range(c - d, c + d):
            A[r - d][j] = A[r - d][j + 1]
        for i in range(r - d, r + d):
            A[i][c + d] = A[i + 1][c + d]
        for j in range(c + d, c - d, -1):
            A[r + d][j] = A[r + d][j - 1]
        for i in range(r + d, r - d, -1):
            A[i][c - d] = A[i - 1][c - d]
        A[r - d + 1][c - d] = temp


def dfs(cnt):
    global ans
    if cnt == k:
        for a in A:
            ans = min(ans, sum(a))
        return

    for i in range(k):
        if not visit[i]:
            r, c, s = cmd_list[i]
            visit[i] = True
            turn(r - 1, c - 1, s)
            dfs(cnt + 1)
            visit[i] = False
            turn2(r - 1, c - 1, s)


n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for x in range(n)]
ans = sys.maxsize

cmd_list = []
visit = [False for _ in range(k)]
for _ in range(k):
    cmd_list.append(list(map(int, input().split())))

dfs(0)
print(ans)
