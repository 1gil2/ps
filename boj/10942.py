#gold 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def go(x, y):
    if x >= y:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    if arr[x] == arr[y]:
        dp[x][y] = go(x+1, y-1)
    else:
        dp[x][y] = 0

    return dp[x][y]


n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

dp = [[-1 for y in range(n+1)] for x in range(n+1)]

for x in range(m):
    s, e = map(int, input().split())
    print(go(s, e))
