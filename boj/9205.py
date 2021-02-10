#silver 1

from collections import deque


def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visit = []
    visit.append([x, y])

    while Q:
        x1, y1 = Q.popleft()

        if x1 == ex and y1 == ey:
            print("happy")
            return
        for nx, ny in L:
            if [nx, ny] not in visit:
                dist = abs(nx - x1) + abs(ny - y1)

                if 1000 >= dist:
                    Q.append([nx, ny])
                    visit.append([nx, ny])
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    L = []
    for i in range(n + 1):
        x, y = map(int, input().split())
        L.append([x, y])

    ex, ey = L[-1][0], L[-1][1]

    bfs(sx, sy)
