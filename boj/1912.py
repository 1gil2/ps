#silver 2

n = int(input())
N = list(map(int, input().split()))

dp = [0 for x in range(n)]
dp[0] = N[0]

for x in range(1, n):
    dp[x] = max(N[x], dp[x-1]+N[x])

print(max(dp))
