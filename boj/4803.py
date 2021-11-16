#gold 4

import sys
input = sys.stdin.readline


def dfs(past, here):
    visit[here] = True
    for there in tree[here]:
        if there == past:
            continue
        if visit[there]:
            return False
        if not dfs(here, there):
            return False
    return True


t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    tree = [[] for x in range(n+1)]
    visit = [False for x in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    cnt = 0
    for x in range(1, n+1):
        if not visit[x]:
            if dfs(0, x):
                cnt += 1

    if cnt == 0:
        print("Case {}: No trees.".format(t))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(t))
    else:
        print("Case {}: A forest of {} trees.".format(t, cnt))
