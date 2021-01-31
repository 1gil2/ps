#gold 1

import sys
input = sys.stdin.readline
inf = 100000007


def tsp(here, address):
    if address == (1 << n) - 1:
        return table[here][0] or inf

    if dp[here][address] is not None:
        return dp[here][address]

    temp = inf

    for x in range(n):
        if address & (1 << x) == 0 and table[here][x] != 0:
            temp = min(temp, tsp(x, address | (1 << x)) + table[here][x])
    dp[here][address] = temp
    return temp


n = int(input())
table = [list(map(int, input().split())) for x in range(n)]
dp = [[None for y in range(1 << n)] for x in range(n)]
#dp[i][j] i 현재위치, j 비트로 방문도시 표현, dp[i][j] 총 이동거리

print(tsp(0, 1))
