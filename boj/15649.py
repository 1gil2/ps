#silver 3

import itertools


def printfz(L):
    for i in L:
        print(i, end=' ')
    print()


n, m = map(int, input().split())
N = list(range(1, n + 1))
p = list(itertools.permutations(N, m))
for x in p:
    printfz(x)
