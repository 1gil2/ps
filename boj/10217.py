#gold 1
#pypy3

import sys

input = sys.stdin.readline
inf = sys.maxsize


def dijk():
    for cost in range(m + 1):
        for here in range(1, n + 1):
            if dp[here][cost] == inf:
                continue

            dist = dp[here][cost]
            for there, cc, dd in table[here]:
                if cost + cc > m:
                    continue

                dp[there][cost + cc] = min(dp[there][cost + cc], dist + dd)

    return


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    # dp[x][y] x도시까지 y비용으로 갈수 있는 최소비용
    dp = [[inf for money in range(m + 1)] for place in range(n + 1)]
    dp[1][0] = 0

    table = [[] for x in range(n + 1)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        table[a].append((b, c, d))

    dijk()

    ans = min(dp[n])
    if ans == inf:
        print("Poor KCM")
    else:
        print(ans)
