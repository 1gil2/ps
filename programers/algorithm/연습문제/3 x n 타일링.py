#level 4


def solution(n):
    if n % 2 == 1:
        return 0
    dp = [0, 3] + [0] * 4999
    for x in range(2, n // 2 + 1):
        temp = 2 + dp[x - 1]
        for y in range(0, x):
            temp += 2 * dp[y]

        dp[x] = temp % 1000000007

    return dp[n // 2]
