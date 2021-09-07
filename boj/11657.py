#gold 4
#pypy3

import sys

input = sys.stdin.readline
inf = sys.maxsize


def bellman():
    global flag

    for repeat in range(m):
        for here in range(1, n + 1):
            for there, cost in table[here]:
                if dist[here] != inf and dist[there] > dist[here] + cost:
                    dist[there] = dist[here] + cost
                    if repeat == n - 1:
                        flag = False


n, m = map(int, input().split())
table = [[] for x in range(n + 1)]
dist = [inf for x in range(n + 1)]
dist[1] = 0
flag = True

for x in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))

bellman()

if not flag:
    print(-1)
else:
    for d in dist[2:]:
        if d == inf:
            print(-1)
        else:
            print(d)
