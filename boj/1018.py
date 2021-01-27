#silver 5


def chess(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if table[x+i][y+j] != color[(i+j) % 2]:
                cnt += 1
    if cnt>=32:
        return 64-cnt
    return cnt


n, m = map(int, input().split())
table = [input() for x in range(n)]
temp = 65
color = ['B', 'W']
for a in range(n-7):
    for b in range(m-7):
        c = chess(a, b)
        if c < temp:
            temp = c
print(temp)
