#silver 3

import sys
input = sys.stdin.readline

n = int(input())
stare = [0 for x in range(301)]
dp = [0 for x in range(301)]

for x in range(n):
    stare[x] = int(input())

dp[0] = stare[0]
dp[1] = stare[0]+stare[1]
dp[2] = max(stare[1]+stare[2], stare[0]+stare[2])
for x in range(3, n):
    dp[x] = max(dp[x-3]+stare[x-1]+stare[x], dp[x-2]+stare[x])

print(dp[n-1])
