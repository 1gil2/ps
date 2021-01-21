#silver 1

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0 for x in range(m+1)] for y in range(n+1)]
dp[0][s] = 1

for x in range(1, n+1):
    for y in range(m+1):
        if dp[x-1][y] == 0:
            continue
        if y+v[x-1] <= m:
            dp[x][y+v[x-1]] = 1
        if y-v[x-1] >= 0:
            dp[x][y-v[x-1]] = 1

ans = -1
for x in range(m+1):
    if dp[n][x] == 1:
        ans = x

print(ans)
