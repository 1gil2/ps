#platinum 5

import sys

input = sys.stdin.readline


def dfs(here):
    visit[here] = True
    for there in F[here]:
        if visit[there]:
            continue
        visit[there] = True
        dfs(there)

    for enemy in E[here]:
        for there in E[enemy]:
            if visit[there]:
                continue
            visit[there] = True
            dfs(there)


n = int(input())
m = int(input())

E = [[] for x in range(n + 1)]
F = [[] for x in range(n + 1)]
visit = [False for x in range(n + 1)]

for _ in range(m):
    cmd, p, q = input().split()
    p = int(p)
    q = int(q)

    if cmd == 'E':
        E[p].append(q)
        E[q].append(p)
    else:
        F[p].append(q)
        F[q].append(p)

ans = 0
for x in range(1, n + 1):
    if not visit[x]:
        dfs(x)
        ans += 1

print(ans)
