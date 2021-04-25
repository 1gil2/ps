#gold 1

n = int(input())
st1 = input()
m = int(input())
st2 = input()

# 9252 LCS2 와 비슷한듯
# dp[x][y] st1[:x], st2[:y]까지의 유사도
dp = [[0 for y in range(m + 1)] for x in range(n + 1)]

M = 0
x1, y1 = 0, 0
for x in range(1, n + 1):
    for y in range(1, m + 1):
        if st1[x - 1] == st2[y - 1]:
            dp[x][y] = dp[x - 1][y - 1] + 3
        else:
            dp[x][y] = max(dp[x][y], dp[x - 1][y] - 2, dp[x][y - 1] - 2, dp[x - 1][y - 1] - 2)

        if dp[x][y] > M:
            M = dp[x][y]
            x1 = x
            y1 = y

# 역추적
x2 = x1
y2 = y1
while True:
    if dp[x2][y2] == 0:
        break
    if dp[x2][y2] == dp[x2 - 1][y2] - 2:
        x2 -= 1
    elif dp[x2][y2] == dp[x2][y2 - 1] - 2:
        y2 -= 1
    else:
        x2 -= 1
        y2 -= 1

print(M)
print(st1[x2:x1])
print(st2[y2:y1])
