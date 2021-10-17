#level 3


def solution(sticker):
    le = len(sticker)
    if le == 1:
        return sticker[0]

    # dp[x][y] x : 0 -> 1번 스티커 O, 1 ->  1번 스티커 X
    # x상황일때 y까지의 최대값
    dp = [[0 for y in range(le)] for x in range(2)]
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    dp[1][1] = sticker[1]

    for x in range(2, le - 1):
        dp[0][x] = max(dp[0][x - 1], dp[0][x - 2] + sticker[x])

    for x in range(2, le):
        dp[1][x] = max(dp[1][x - 1], dp[1][x - 2] + sticker[x])

    m1 = max(dp[0])
    m2 = max(dp[1])

    return max(m1, m2)
