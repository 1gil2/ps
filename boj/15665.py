#silver 2


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, A)))
        return
    for x in num:
        A.append(x)
        dfs(depth + 1)
        A.pop()


n, m = map(int, input().split())

num = list(set(map(int, input().split())))
num.sort()

A = []
dfs(0)
