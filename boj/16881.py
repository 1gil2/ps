#platinum 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

xor = 0

for _ in range(n):
    game = list(map(int, input().split()))

    dp = [-1 for x in range(m+1)]

    dp[m] = game[m-1]

    for x in range(m-1, 0, -1):
        if dp[x+1] == 0:
            dp[x] = game[x-1]
        else:
            if game[x-1] > dp[x+1]:
                dp[x] = game[x-1]
            else:
                dp[x] = game[x-1] - 1

    xor ^= dp[1]

if xor:
    print("koosaga")
else:
    print("cubelover")
