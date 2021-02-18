#gold 5

n, k = map(int, input().split())

item = [[0, 0]]
for x in range(1, n+1):
    item.append(list(map(int, input().split())))

dp = [[0] * (k+1) for x in range(n+1)]

for x in range(1, n+1):
    for y in range(1, k+1):
        if y >= item[x][0]:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-item[x][0]] + item[x][1])
        else:
            dp[x][y] = dp[x-1][y]

print(dp[n][k])
