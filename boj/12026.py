#silver 1

n = int(input())
block = input()

dp = [-1 for x in range(n)]

dp[0] = 0

for x in range(1, n):
    if block[x] == 'B':
        for y in range(x):
            if block[y] == 'J':
                if dp[y] == -1:
                    continue
                else:
                    if dp[x] == -1:
                        dp[x] = dp[y]+(x-y)*(x-y)
                    else:
                        dp[x] = min(dp[x], dp[y]+(x-y)*(x-y))
    elif block[x] == 'O':
        for y in range(x):
            if block[y] == 'B':
                if dp[y] == -1:
                    continue
                else:
                    if dp[x] == -1:
                        dp[x] = dp[y]+(x-y)*(x-y)
                    else:
                        dp[x] = min(dp[x], dp[y]+(x-y)*(x-y))
    elif block[x] == 'J':
        for y in range(x):
            if block[y] == 'O':
                if dp[y] == -1:
                    continue
                else:
                    if dp[x] == -1:
                        dp[x] = dp[y]+(x-y)*(x-y)
                    else:
                        dp[x] = min(dp[x], dp[y]+(x-y)*(x-y))

print(dp[-1])
