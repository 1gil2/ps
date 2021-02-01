#silver 1

t, w = map(int, input().split())

jadu = [[0]*1002 for x in range(3)] #위치, 초
dp = [[[0]*1002 for x in range(3)] for y in range(33)] #dp[이동수][위치][초]=먹은 자두

for x in range(t):
    jadu[int(input())][x+1] = 1

dp[0][1][1] = jadu[1][1]
dp[1][2][1] = jadu[2][1]

M = max(dp[0][1][1], dp[1][2][1])

for x in range(2, t+1):
    for y in range(w+1):
        dp[y][1][x] = max(dp[y][1][x-1], dp[y-1][2][x-1])+jadu[1][x]
        dp[y][2][x] = max(dp[y][2][x-1], dp[y-1][1][x-1])+jadu[2][x]

        M = max(M, dp[y][1][x])
        M = max(M, dp[y][2][x])

print(M)
