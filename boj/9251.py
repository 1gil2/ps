#gold 5

s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

dp = [[0 for y in range(1001)] for x in range(1001)]

flag = 0
for x in range(l1):
    if s2[0] == s1[x]:
        flag = 1
    dp[x][0] = flag
dp[l1][0] = flag

flag = 0
for x in range(l2):
    if s2[x] == s1[0]:
        flag = 1
    dp[0][x] = flag
dp[0][l2] = flag

for x in range(1, l1):
    for y in range(1, l2):
        if s1[x] == s2[y]:
            dp[x][y] = dp[x-1][y-1] +1
        else:
            dp[x][y] = max(dp[x-1][y-1], dp[x-1][y], dp[x][y-1])

print(dp[l1-1][l2-1])