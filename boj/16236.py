#gold 4

from heapq import heappop, heappush

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

n = int(input())
pool = [list(map(int, input().split())) for x in range(n)]
q = []

for y in range(n):
    for x in range(n):
        if pool[y][x] == 9:
            heappush(q, (0, y, x))
            pool[y][x] = 0

size = 2
cnt = 0
ans = 0
visit = [[0 for x in range(n)] for y in range(n)]

while q:
    d, y, x = heappop(q)
    if 0 < pool[y][x] < size:
        cnt += 1
        pool[y][x] = 0
        if cnt == size:
            size += 1
            cnt = 0
        ans += d
        d = 0
        q = []
        visit = [[0 for x in range(n)] for y in range(n)]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[ny][nx] == 0 and pool[ny][nx] <= size:
            visit[ny][nx] = 1
            heappush(q, (d + 1, ny, nx))

print(ans)
