#level 3


def solution(n):
    dp = [0, 1, 2]
    if n < 3:
        return dp[n]
    for x in range(3, n + 1):
        dp.append((dp[x - 1] + dp[x - 2]) % 1234567)

    return dp[n]
