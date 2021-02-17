#platinum 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(here, r):
    global number
    number += 1
    order[here] = number
    ret = order[here]
    child = 0

    for there in graph[here]:
        if order[there]:
            ret = min(ret, order[there])
            continue

        child += 1
        prev = dfs(there, 0)

        if r == 0 and prev >= order[here]:
            check[here] = 1

        ret = min(ret, prev)

    if r == 1 and child >= 2:
        check[here] = 1

    return ret


v, e = map(int, input().split())
graph = [[] for x in range(v+1)]
order = [0 for x in range(v+1)]
check = [0 for x in range(v+1)]
number = 0
cnt = 0

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(1, v+1):
    if order[x] == 0:
        dfs(x, 1)

for x in range(1, v+1):
    if check[x]:
        cnt += 1

print(cnt)
for x in range(v+1):
    if check[x]:
        print(x, end=' ')
