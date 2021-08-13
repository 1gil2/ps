#gold 2

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
table = [list(input().rstrip()) for x in range(m)]

things = 0
thing_list = []
for x in range(m):
    for y in range(n):
        if table[x][y] == 'S':
            sx, sy = x, y
        elif table[x][y] == 'E':
            ex, ey = x, y
        elif table[x][y] == 'X':
            table[x][y] = str(things)
            thing_list.append((x, y))
            things += 1

end = 2 ** things - 1
visit = [[[0 for z in range(2 ** things)] for y in range(n)] for x in range(m)]
visit[sx][sy][0] = 1

dq = deque()
dq.append((sx, sy, 0, 0))

while dq:
    x, y, cnt, state = dq.popleft()

    if x == ex and y == ey and state == end:
        print(cnt)
        break

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        if 0 <= x1 < m and 0 <= y1 < n and table[x1][y1] != '#':
            if (x1, y1) in thing_list:
                th = int(table[x1][y1])
                nxt_state = state | (1 << th)
                if visit[x1][y1][nxt_state] == 0:
                    visit[x1][y1][nxt_state] = 1
                    dq.append((x1, y1, cnt+1, nxt_state))
            else:
                if visit[x1][y1][state] == 0:
                    visit[x1][y1][state] = 1
                    dq.append((x1,y1, cnt+1, state))
