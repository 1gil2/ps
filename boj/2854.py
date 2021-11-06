#gold 4

import sys
input = sys.stdin.readline
mod = 1000000007

n = int(input())
p1 = [0] + list(map(int, input().split()))
p2 = [0] + list(map(int, input().split())) + [0]

#dp[x][0] x번 문제를 x로 출제
#dp[x][1] x번 문제를 x-0.5로 출제
#dp[x][2] x번 문제를 x+0.5로 출제
dp = [[0 for y in range(3)] for x in range(n+1)]

dp[1][0] = p1[1]
dp[1][1] = 0
dp[1][2] = p2[1]

for x in range(2, n+1):
    dp[x][0] = (sum(dp[x-1]) * p1[x]) % mod
    dp[x][1] = ((dp[x-1][0]+dp[x-1][1]) * p2[x-1] + dp[x-1][2] * (p2[x-1] - 1)) % mod
    dp[x][2] = (sum(dp[x-1]) * p2[x]) % mod

print(sum(dp[n]) % mod)
