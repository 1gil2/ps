#silver 3


def dfs(a, n, L):
    if a == m:
        for x in L:
            print(x, end=' ')
        print()
        return
    for i in A:
        if i <= n:
            continue
        else:
            L.append(i)
            dfs(a+1, i, L)
            if len(L) > a:
                L.pop(a)


n, m = map(int, input().split())
A = list(range(1, n+1))
for x in A:
    L = [x]
    dfs(1, x, L)
