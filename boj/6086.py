#platinum 4

import sys
from collections import deque
input = sys.stdin.readline


def change(st):
    if st.isupper():
        return ord(st) - ord('A')
    return ord(st) - ord('a') + 26


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
        visit = [-1 for x in range(52)]
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


n = int(input())
capacity = [[0 for y in range(52)] for x in range(52)]
flow = [[0 for y in range(52)] for x in range(52)]
table = [[] for x in range(52)]

for _ in range(n):
    a, b, c = input().rstrip().split()

    a = change(a)
    b = change(b)

    capacity[a][b] += int(c)
    capacity[b][a] += int(c)
    table[a].append(b)
    table[b].append(a)

source = change('A')
sink = change('Z')

print(edmond(source, sink))
