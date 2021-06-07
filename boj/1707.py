#gold 4

import sys
from collections import deque
input = sys.stdin.readline


def bfs(idx):
    visit[idx] = 1
    dq = deque()
    dq.append(idx)

    while dq:
        k = dq.popleft()
        for x in table[k]:
            if visit[x] == 0:
                visit[x] = -visit[k]
                dq.append(x)
            else:
                if visit[x] == visit[k]:
                    return False

    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    flag = True

    table = [[] for x in range(v + 1)]
    for x in range(e):
        a, b = map(int, input().split())
        table[a].append(b)
        table[b].append(a)

    visit = [0 for x in range(v + 1)]
    for x in range(1, v + 1):
        if visit[x] == 0:
            if not bfs(x):
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")
