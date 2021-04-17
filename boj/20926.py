#gold 2
#pypy3

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 미끄러지는 이동을 구현함
def move(x, y, i):
    cnt = 0
    while True:
        x += dx[i]
        y += dy[i]

        if table[x][y] == 'H':
            return False, 0, 0, 0
        if table[x][y] == 'R':
            return True, cnt, x - dx[i], y - dy[i]
        if table[x][y] == 'E':
            return True, cnt, x, y
        if int(table[x][y]) == -1:
            return False, 0, 0, 0
        cnt += int(table[x][y])


# 함수이름이 bfs가 아니라 dijk이 맞는듯
def bfs():
    visit = [[sys.maxsize for y in range(w + 2)] for x in range(h + 2)]
    visit[sx][sy] = 0
    heap = []
    heappush(heap, (0, sx, sy))

    while heap:
        time, x, y = heappop(heap)

        for i in range(4):
            flag, cnt, x1, y1 = move(x, y, i)

            if flag and visit[x1][y1] > time + cnt:
                visit[x1][y1] = time + cnt
                heappush(heap, (time + cnt, x1, y1))

    if visit[ex][ey] == sys.maxsize:
        print(-1)
    else:
        print(visit[ex][ey])

    return


w, h = map(int, input().split())
table = []
# 작업하기 편하게 주변을 -1로 둘러쌈
table.append([-1 for x in range(w + 2)])
for x in range(h):
    temp1 = input().strip()
    temp2 = [-1]
    for k in temp1:
        temp2.append(k)
    temp2.append(-1)
    table.append(temp2)
table.append([-1 for x in range(w + 2)])

for x in range(h + 2):
    for y in range(w + 2):
        if table[x][y] == 'T':
            table[x][y] = 0
            sx = x
            sy = y
        if table[x][y] == 'E':
            ex = x
            ey = y

bfs()