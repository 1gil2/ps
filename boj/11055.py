#silver 2

n = int(input())

num = list(map(int, input().split()))

dp = [num[x] for x in range(n)]

for x in range(1, n):
    temp = 0
    for y in range(x):
        if num[x] > num[y]:
            temp = max(temp, dp[y])
    dp[x] += temp

print(max(dp))
