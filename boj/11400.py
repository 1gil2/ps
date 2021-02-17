#platinum 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(here, parent):
    global number
    number += 1
    order[here] = number
    ret = order[here]

    for there in graph[here]:

        if there == parent:
            continue

        if order[there]:
            ret = min(ret, order[there])
            continue

        prev = dfs(there, here)

        if prev > order[here]:
            check.append((min(here, there), max(here, there)))

        ret = min(ret, prev)

    return ret


v, e = map(int, input().split())
graph = [[] for x in range(v+1)]
order = [0 for x in range(v+1)]
check = []
number = 0
cnt = 0

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(1, v+1):
    if order[x] == 0:
        dfs(x, 0)

check.sort()

print(len(check))
for x, y in check:
    print(x, y)
