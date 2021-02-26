#silver 2


def dfs(idx, depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return

    post = 0
    for x in range(idx, n):
        if visit[x] == 0 and post != L[x]:
            visit[x] = 1
            answer.append(L[x])
            post = L[x]
            dfs(x+1, depth+1)
            visit[x] = 0
            answer.pop()


n, m = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

visit = [0 for x in range(n)]
answer = []

dfs(0, 0)
