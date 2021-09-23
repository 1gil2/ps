#level 4


def solution(money):
    lm = len(money)
    dp1 = [0] * lm
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for x in range(2, lm - 1):
        dp1[x] = max(dp1[x - 1], money[x] + dp1[x - 2])

    dp2 = [0] * lm
    dp2[0] = 0
    dp2[1] = money[1]

    for x in range(2, lm):
        dp2[x] = max(dp2[x - 1], money[x] + dp2[x - 2])

    return max(max(dp1), max(dp2))
