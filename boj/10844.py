#silver 1

n = int(input())
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for x in range(n - 1):
    dp.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for y in range(10):
        if y == 0:
            dp[x + 1][0] = dp[x][1]
        elif y == 9:
            dp[x + 1][9] = dp[x][8]
        else:
            dp[x + 1][y] = dp[x][y - 1] + dp[x][y + 1]

print(sum(dp[-1]) % 1000000000)
