#silver 3

n = int(input())
dp = [0, 1, 2, 3]
m = 15746

if n < 4:
    print(dp[n])
else:
    for x in range(n-3):
        dp.append((dp[-1]+dp[-2])%m)
    print(dp[-1])
