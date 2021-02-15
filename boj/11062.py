#gold 3
#pypy3

import sys
input = sys.stdin.readline


def solve(s, e):
    if s == e:
        return card[s]

    if dp[s][e] != -1:
        return dp[s][e]

    ret = 0
    ret = solve2(s, e-1) + card[e]
    ret = max(ret, solve2(s+1, e) + card[s])
    dp[s][e] = ret
    return ret


def solve2(s, e):
    if s == e:
        return 0

    ret = 0
    ret = solve(s, e-1)
    ret = min(ret, solve(s+1, e))
    return ret


t = int(input())
for _ in range(t):
    n = int(input())
    card = list(map(int, input().split()))

    dp = [[-1 for y in range(n+1)] for x in range(n+1)]

    print(solve(0, n-1))
