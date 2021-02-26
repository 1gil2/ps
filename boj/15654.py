#silver 3


def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, L)))
        return

    for x in range(n):
        if visit[x] == 0:
            visit[x] = 1
            L.append(num[x])
            dfs(depth+1, n, m)
            L.pop()
            visit[x] = 0


n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

visit = [0]*n
L = []

dfs(0, n, m)
