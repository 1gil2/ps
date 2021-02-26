#silver 2


def dfs(depth, idx):
    if depth == m:
        print(' '.join(map(str, A)))
        return
    for x in range(idx, le):
        A.append(num[x])
        dfs(depth + 1, x)
        A.pop()


n, m = map(int, input().split())

num = list(set(map(int, input().split())))
num.sort()
le = len(num)

A = []
dfs(0, 0)
