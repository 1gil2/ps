#silver 3


def dfs(depth, idx):
    if depth == m:
        print(' '.join(map(str, A)))
        return

    for x in range(idx, n):
        visit[x] = 1
        A.append(L[x])
        dfs(depth+1, x)
        A.pop()
        visit[x] = 0


n, m = map(int, input().split())

L = list(map(int, input().split()))
L.sort()

A = []
visit = [0]*n

dfs(0, 0)
