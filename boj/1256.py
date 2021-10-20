#gold 3

import sys

input = sys.stdin.readline


def solution(n, m, k):
    # dp[x][y] (가 x개, )가 y개
    dp = [[1 for y in range(m + 1)] for x in range(n + 1)]

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

    answer = ""
    if dp[n][m] < k:
        return -1

    while True:
        if n == 0 or m == 0:
            answer += 'z' * m
            answer += 'a' * n
            break

        temp = dp[n - 1][m]
        if k <= temp:
            answer += 'a'
            n -= 1
        else:
            answer += 'z'
            m -= 1
            k -= temp

    return answer


n, m, k = map(int, input().split())
print(solution(n, m, k))
