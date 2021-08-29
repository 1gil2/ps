#platinum 3

import sys
input = sys.stdin.readline


def go(problem, time):
    if problem == n:
        return 0

    ret = dp[problem][time]
    if ret != -1:
        return ret

    ret = go(problem + 1, time)
    dp[problem][time] = ret

    temp = problems[problem]

    if time + temp[2] <= t:
        ret = max(ret, temp[0] - (time + temp[2]) * temp[1] + go(problem + 1, time + temp[2]))

    dp[problem][time] = ret
    return ret


n, t = map(int, input().split())

M = list(map(int, input().split()))
P = list(map(int, input().split()))
R = list(map(int, input().split()))

problems = [(M[i], P[i], R[i]) for i in range(n)]
problems.sort(key=lambda x: x[2] / x[1])

# dp[x][y] x문제를 y시간에서 얻을 수 있는 최대 점수
dp = [[-1 for time in range(t + 1)] for problem in range(n + 1)]

print(go(0, 0))
