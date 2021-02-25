#silver 3
#pypy3

import sys


def back(idx, cnt):
    global ans
    if cnt == m:
        start, link = 0, 0
        for x in range(n):
            for y in range(n):
                if visit[x] == 1 and visit[y] == 1:
                    start += table[x][y]
                elif visit[x] == 0 and visit[y] == 0:
                    link += table[x][y]
        ans = min(ans, abs(start-link))

    for x in range(idx, n):
        if visit[x]:
            continue
        visit[x] = 1
        back(x+1, cnt+1)
        visit[x] = 0


n = int(sys.stdin.readline())
m = n//2
table = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

visit = [0 for x in range(n)]
ans = 987654321

back(0, 0)
print(ans)
