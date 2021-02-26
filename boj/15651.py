#silver 3


def abc(m):
    if m == 0:
        for a in L:
            print(a, end=' ')
        L.pop()
        print()
        return
    for x in A:
        L.append(x)
        abc(m-1)
    if len(L) != 0:
        L.pop()


n, m = map(int, input().split())

A = [x for x in range(1,n+1)]

L = []
abc(m)
