#level 2


def solution(land):
    land_len = len(land)
    dp = [[0 for y in range(4)] for x in range(land_len)]

    for x in range(4):
        dp[0][x] = land[0][x]

    # x 층, y 몇 번째 칸, z 반복
    for x in range(1, land_len):
        for y in range(4):
            for z in range(4):
                if y == z:
                    continue
                dp[x][y] = max(dp[x][y], land[x][y] + dp[x - 1][z])

    return max(dp[-1])
