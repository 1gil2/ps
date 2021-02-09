#silver 2


def dfs(a, n, L):
    if a == 6:
        for p in L:
            print(p, end=' ')
        print()
        L.pop()
        return
    for i in s:
        if i <= n:
            continue
        else:
            L.append(i)
            dfs(a+1, i, L)
            if len(L) > a:
                L.pop()


while True:
    A = list(map(int, input().split()))
    k = A[0]
    if k == 0:
        break
    s = A[1:]
    for x in s:
        L = [x]
        dfs(1, x, L)
    print()
