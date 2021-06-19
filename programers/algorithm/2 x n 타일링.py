#level 3


def solution(n):
    dp1 = [0, 1, 1]
    dp2 = [0, 0, 1]
    if n < 3:
        return dp1[n] + dp2[n]
    for x in range(3, n + 1):
        dp1.append((dp1[x - 1] + dp2[x - 1]) % 1000000007)
        dp2.append((dp1[x - 2] + dp2[x - 2]) % 1000000007)

    return (dp1[n] + dp2[n]) % 1000000007
