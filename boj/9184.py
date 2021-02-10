#silver 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def w(a, b, c):
    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        dp[a][b][c] = w(20, 20, 20)
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


dp = [[[-1 for z in range(101)] for y in range(101)] for x in range(101)]


while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print('w(', x, ', ', y, ', ', z, ') = ', w(x, y, z), sep='')
