#silver 1

n = int(input())

dp = [[0 for x in range(10)] for y in range(n)]

dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for x in range(1, n):
    for y in range(10):
        if y == 0:
            dp[x][0] = 1
        else:
            dp[x][y] = (dp[x][y-1]+dp[x-1][y]) % 10007

ans = 0
for x in range(10):
    ans += dp[-1][x]
print(ans % 10007)
