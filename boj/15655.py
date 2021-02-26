#silver 3


def dfs(idx, depth):
    if depth == m:
        print(' '.join(map(str, num)))
        return

    for x in range(idx, n):
        if visit[x] == 0:
            visit[x] = 1
            num.append(L[x])
            dfs(x+1, depth+1)
            num.pop()
            visit[x] = 0


n, m = map(int, input().split())

L = list(map(int, input().split()))
L.sort()

visit = [0]*n
num = []

dfs(0, 0)
