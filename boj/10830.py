#gold 4

import sys
input = sys.stdin.readline


def go(cnt):
    res = [[0 for x in range(n)] for y in range(n)]
    c = [[0 for x in range(n)] for y in range(n)]

    if cnt == 1:
        for x in range(n):
            for y in range(n):
                c[x][y] = A[x][y] % 1000
        return c
    elif cnt % 2 == 0:
        c = go(cnt//2)
        for x in range(n):
            for y in range(n):
                for k in range(n):
                    res[x][y] += c[x][k] * c[k][y]

                res[x][y] %= 1000
        return res
    else:
        c = go(cnt-1)
        for x in range(n):
            for y in range(n):
                for k in range(n):
                    res[x][y] += c[x][k] * A[k][y]

                res[x][y] %= 1000
        return res


n, b = map(int, input().split())
A = [list(map(int, input().split())) for x in range(n)]

ans = go(b)

for x in range(n):
    for y in range(n):
        print(ans[x][y], end=' ')
    print()
