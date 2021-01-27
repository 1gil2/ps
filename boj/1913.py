#silver 5

n = int(input())
m = int(input())
a = b = n//2
snail = [[0 for x in range(n)] for y in range(n)]

cnt = 1
leng = 1
drc = 1
snail[a][b] = cnt

while True:
    if drc == 1:
        for x in range(leng):
            cnt += 1
            a -= 1
            snail[a][b] = cnt
            if cnt == n*n:
                break
        drc = 2
        if cnt == n*n:
            break
    elif drc == 2:
        for x in range(leng):
            cnt += 1
            b += 1
            snail[a][b] = cnt
        drc = 3
        leng += 1
    elif drc == 3:
        for x in range(leng):
            cnt += 1
            a += 1
            snail[a][b] = cnt
        drc = 4
    else:
        for x in range(leng):
            cnt += 1
            b -= 1
            snail[a][b] = cnt
        drc = 1
        leng += 1

for x in range(n):
    for y in range(n):
        print(snail[x][y], end=' ')
        if snail[x][y] == m:
            c = x+1
            d = y+1
    print()
print(c, d)
