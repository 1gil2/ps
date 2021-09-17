#level 4

import sys


def solution(strs, t):
    n = len(t)
    dp = [sys.maxsize for x in range(n + 1)]
    dp[0] = 0

    for i in range(n):
        start = i

        for j in range(1, 6):
            end = start + j
            if end > n:
                break

            st = t[start:end]
            if st in strs:
                dp[end] = min(dp[end], dp[start] + 1)

    if dp[-1] == sys.maxsize:
        return -1
    return dp[-1]
