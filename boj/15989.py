#silver 1

#dp[x][y] x수를 만드는 제일 큰 수가 y
dp = [[0 for y in range(4)] for x in range(10001)]

dp[0][1] = 0
dp[0][2] = 0
dp[0][3] = 0

dp[1][1] = 1
dp[1][2] = 0
dp[1][3] = 0

dp[2][1] = 1
dp[2][2] = 1
dp[2][3] = 0

dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for x in range(4, 10001):
    dp[x][1] = 1
    dp[x][2] = 1 + dp[x-2][2]
    dp[x][3] = 1 + dp[x-3][2] + dp[x-3][3]


t= int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][1] + dp[n][2]+ dp[n][3])
