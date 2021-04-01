#silver 1

n = int(input())

dp = [[0 for y in range(3)] for x in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for x in range(2, n+1):
    dp[x][0] = (dp[x-1][1]+dp[x-1][2])%9901
    dp[x][1] = (dp[x-1][0]+dp[x-1][2])%9901
    dp[x][2] = (dp[x-1][0]+dp[x-1][1]+dp[x-1][2])%9901

print((dp[n][0]+dp[n][1]+dp[n][2])%9901)
