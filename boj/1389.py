#silver 1

n, m = map(int, input().split())
table = [[n for x in range(n)] for y in range(n)]

for x in range(m):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1
    table[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                table[i][j] = 0
            else:
                table[i][j] = min(table[i][j], table[i][k]+table[k][j])

ans = []
for x in table:
    ans.append(sum(x))

print(ans.index(min(ans))+1)
