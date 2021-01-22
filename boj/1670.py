#gold 2

n = int(input())

dp = [0 for x in range(n+1)]

dp[0] = 1
dp[2] = 1
dp[4] = 2

for x in range(6, n+1, 2):
    ret = 0
    for y in range(x//4):
        ret += dp[2*y]*dp[x-2*y-2]*2

    if x%4 == 2:
        ret += dp[(x-2)//2]*dp[(x-2)//2]

    dp[x] = ret%987654321

print(dp[n])
