#gold 2

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dist[s] = 0
    dq = deque()
    dq.append(s)

    if s == e:
        print(0)
        return

    while dq:
        here = dq.popleft()

        if here == e:
            print(dist[e]-1)
            return

        for there, cost in table[here]:
            temp = dist[here] + cost
            if dist[there] > temp:
                dist[there] = temp
                if cost:
                    dq.append(there)
                else:
                    dq.appendleft(there)

    print(-1)
    return


n, m = map(int, input().split())
dist = [sys.maxsize for x in range(n+m+1)]
table = [[] for x in range(n+m+1)]

for x in range(m):
    temp = list(map(int, input().split()))
    for node in temp:
        if node == -1:
            break
        table[node].append((n+x+1, 1))
        table[n+x+1].append((node, 0))

s, e = map(int, input().split())

bfs()
