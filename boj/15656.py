#silver 3


def dfs(idx, depth):
    if depth == m:
        print(' '.join(map(str, num)))
        return

    for x in range(n):
        num.append(L[x])
        dfs(x + 1, depth + 1)
        num.pop()


n, m = map(int, input().split())

L = list(map(int, input().split()))
L.sort()

num = []

dfs(0, 0)
