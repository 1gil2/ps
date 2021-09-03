#gold 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def go(state, artist, cost):
    if dp[state][artist][cost] != -1:
        return dp[state][artist][cost]

    ret = 1
    for nxt, buy in enumerate(table[artist]):
        if not state & (1 << nxt) and int(buy) >= cost:
            ret = max(ret, go(state | (1 << nxt), nxt, int(buy)) + 1)

    dp[state][artist][cost] = ret
    return ret


n = int(input())
table = [list(input().rstrip()) for x in range(n)]

# dp[bit-visit][artist][cost] bit상태일때 artist이 cost비용으로 사는 최대값
dp = [[[-1 for cost in range(10)] for artist in range(n + 1)] for bit in range(1 << n)]

print(go(1, 0, 0))
