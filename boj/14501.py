#silver 4

n = int(input())
T = []
P = []

for x in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp = [0] * n

if T[n - 1] == 1:
    dp[n - 1] = P[n - 1]

for x in range(n - 2, -1, -1):

    day = x + T[x]

    if day == n:
        dp[x] = max(P[x], dp[x + 1])
    elif day > n:
        dp[x] = dp[x + 1]
    else:
        dp[x] = max(P[x] + dp[day], dp[x + 1])

print(dp[0])
