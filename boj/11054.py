#gold 3

n = int(input())

num = list(map(int, input().split()))

dp = [1]*n

for x in range(1, n):
    for y in range(x):
        if num[x] > num[y]:
            dp[x] = max(dp[x], dp[y]+1)

num2 = num[::-1]

dp2 = [1]*n

for x in range(1, n):
    for y in range(x):
        if num2[x] > num2[y]:
            dp2[x] = max(dp2[x], dp2[y]+1)

M = 0
for x in range(n):
    M = max(M, dp[x]+dp2[-(x+1)])

print(M-1)
