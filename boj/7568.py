#silver 5

big = []
n = int(input())
for t in range(n):
    big.append(list(map(int, input().split())))

for x in range(n):
    cnt = 1
    for y in range(n):
        if big[x][0] < big[y][0] and big[x][1] < big[y][1]:
            cnt += 1
    print(cnt, end=' ')
