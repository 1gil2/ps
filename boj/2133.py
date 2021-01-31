#silver 1

n = int(input())

dp = [0 for x in range(50)]

dp[0] = 1
dp[2] = 3

for x in range(4, n+1, 2):
    dp[x] = dp[x-2]
    for y in range(2, x+1, 2):
        dp[x] += dp[x-y]*2

print(dp[n])
