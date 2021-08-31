#platinum 4

import sys
from collections import deque
input = sys.stdin.readline


def bfs(source, sink, visit):
    dq = deque()
    dq.append(source)

    while dq and visit[sink] == -1:
        here = dq.popleft()

        for there in table[here]:
            if capacity[here][there] > flow[here][there] and visit[there] == -1:
                dq.append(there)
                visit[there] = here

                if there == sink:
                    break

    if visit[sink] == -1:
        return True
    else:
        return False


def edmond(source, sink):
    ans = 0

    while True:
        visit = [-1 for x in range(n+1)]
        if bfs(source, sink, visit):
            break

        minFlow = sys.maxsize

        i = sink
        while i != source:
            minFlow = min(minFlow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]

        i = sink
        while i != source:
            flow[visit[i]][i] += minFlow
            flow[i][visit[i]] -= minFlow
            i = visit[i]

        ans += minFlow

    return ans


n, m = map(int, input().split())
capacity = [[0 for y in range(n+1)] for x in range(n+1)]
flow = [[0 for y in range(n+1)] for x in range(n+1)]
table = [[] for x in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    capacity[a][b] += c
    capacity[b][a] += c
    table[a].append(b)
    table[b].append(a)

print(edmond(1, n))
