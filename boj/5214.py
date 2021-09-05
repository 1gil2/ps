#gold 1

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((1, 1))

    while q:
        here, cnt = q.popleft()

        if here == n:
            print(cnt)
            return

        for there in table[here]:
            if visit[there] == 1:
                continue

            if there > n:
                visit[there] = 1
                q.append((there, cnt))
            else:
                visit[there] = 1
                q.append((there, cnt + 1))

    print(-1)
    return


n, k, m = map(int, input().split())

table = [[] for x in range(n + m + 2)]
visit = [0 for x in range(n + m + 2)]
visit[1] = 1

for x in range(1, m + 1):
    stations = list(map(int, input().split()))
    for station in stations:
        table[station].append((x + n + 1))
        table[x + n + 1].append((station))

bfs()
