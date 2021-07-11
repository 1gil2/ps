#level 3


def solution(n, money):
    ml = len(money)
    # dp[x][y] x까지의 동전으로 y원을 만드는 개수
    dp = [[0 for y in range(n + 1)] for x in range(ml)]
    dp[0][0] = 1

    for x in range(money[0], n + 1, money[0]):
        dp[0][x] = 1

    for x in range(1, ml):
        for y in range(n + 1):
            if y >= money[x]:
                dp[x][y] = dp[x - 1][y] + dp[x][y - money[x]]
            else:
                dp[x][y] = dp[x - 1][y]

    return dp[-1][-1]
