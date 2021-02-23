#gold 5

n, m = map(int, input().split())

table = [list(map(int, input().split())) for x in range(n)]

ans = 0

# 4*1
for x in range(n - 3):
    for y in range(m):
        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 2][y] + table[x + 3][y])

# 1*4
for x in range(n):
    for y in range(m - 3):
        ans = max(ans, table[x][y] + table[x][y + 1] + table[x][y + 2] + table[x][y + 3])

# 2*2
for x in range(n - 1):
    for y in range(m - 1):
        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 1][y + 1] + table[x][y + 1])

# in 3*3
for x in range(n - 2):
    for y in range(m - 2):
        # 1*3
        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 2][y] + table[x][y + 1])
        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 2][y] + table[x + 1][y + 1])
        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 2][y] + table[x + 2][y + 1])

        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x][y])
        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 1][y])
        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 2][y])
        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x][y + 2])
        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 1][y + 2])
        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 2][y + 2])

        ans = max(ans, table[x][y + 2] + table[x + 1][y + 2] + table[x + 2][y + 2] + table[x][y + 1])
        ans = max(ans, table[x][y + 2] + table[x + 1][y + 2] + table[x + 2][y + 2] + table[x + 1][y + 1])
        ans = max(ans, table[x][y + 2] + table[x + 1][y + 2] + table[x + 2][y + 2] + table[x + 2][y + 1])

        # 3*1
        ans = max(ans, table[x][y] + table[x][y + 1] + table[x][y + 2] + table[x + 1][y])
        ans = max(ans, table[x][y] + table[x][y + 1] + table[x][y + 2] + table[x + 1][y + 1])
        ans = max(ans, table[x][y] + table[x][y + 1] + table[x][y + 2] + table[x + 1][y + 2])

        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x][y])
        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x][y + 1])
        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x][y + 2])
        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x + 2][y])
        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x + 2][y + 1])
        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x + 2][y + 2])

        ans = max(ans, table[x + 2][y] + table[x + 2][y + 1] + table[x + 2][y + 2] + table[x + 1][y])
        ans = max(ans, table[x + 2][y] + table[x + 2][y + 1] + table[x + 2][y + 2] + table[x + 1][y + 1])
        ans = max(ans, table[x + 2][y] + table[x + 2][y + 1] + table[x + 2][y + 2] + table[x + 1][y + 2])

        # Z
        ans = max(ans, table[x][y] + table[x][y + 1] + table[x + 1][y + 1] + table[x + 1][y + 2])
        ans = max(ans, table[x][y + 2] + table[x][y + 1] + table[x + 1][y + 1] + table[x + 1][y])

        ans = max(ans, table[x + 1][y] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 2][y + 2])
        ans = max(ans, table[x + 1][y + 2] + table[x + 1][y + 1] + table[x + 2][y + 1] + table[x + 2][y])

        ans = max(ans, table[x][y] + table[x + 1][y] + table[x + 1][y + 1] + table[x + 2][y + 1])
        ans = max(ans, table[x + 2][y] + table[x + 1][y] + table[x + 1][y + 1] + table[x][y + 1])

        ans = max(ans, table[x][y + 1] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x + 2][y + 2])
        ans = max(ans, table[x + 2][y + 1] + table[x + 1][y + 1] + table[x + 1][y + 2] + table[x][y + 2])

print(ans)
