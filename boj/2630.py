#silver 3


def dc(x, y, N):
    if paper(x, y, N):
        ans[table[x][y]] += 1
        return
    k = N // 2
    for a in range(2):
        for b in range(2):
            dc(x + k * a, y + k * b, k)


def paper(x, y, N):
    for i in range(x, x + N):
        for j in range(y, y + N):
            if table[x][y] != table[i][j]:
                return False
    return True


n = int(input())
table = []
for x in range(n):
    table.append(list(map(int, input().split())))

ans = [0, 0]
dc(0, 0, n)
print(ans[0], ans[1])
