#gold 1

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def solve(light):
    global cnt

    ret = dp[light]
    if ret != -1:
        return ret
    if cnt >= p:
        dp[light] = 0
        return 0

    ret = sys.maxsize

    for i in range(n):
        if light & (1 << i):
            for j in range(n):
                if not light & (1 << j):
                    cnt += 1
                    ret = min(ret, solve(light | (1 << j)) + table[i][j])
                    cnt -= 1

    dp[light] = ret
    return ret


n = int(input())
table = [list(map(int, input().split())) for x in range(n)]
init = input().rstrip()
p = int(input())
dp = [-1 for x in range(1 << (n + 1))]

cnt = 0
start = 0
for i, x in enumerate(init):
    if x == 'Y':
        cnt += 1
        start |= 1 << i

ans = solve(start)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
