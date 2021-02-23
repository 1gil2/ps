#gold 5


def roll(vec):
    if vec == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif vec == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif vec == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif vec == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


n, m, x, y, k = map(int, input().split())

table = [list(map(int, input().split())) for x in range(n)]

cmd = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0] #0 아래 북 동 서 남 위

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in cmd:
    x1 = x+dx[i]
    y1 = y+dy[i]

    if 0 <= x1 < n and 0 <= y1 < m:
        x = x1
        y = y1
        roll(i)
        if table[x][y] != 0:
            dice[1] = table[x][y]
            table[x][y] = 0
        else:
            table[x][y] = dice[1]
        print(dice[6])
