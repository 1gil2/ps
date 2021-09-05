#gold 3

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, m, p = map(int, input().split())

    table = [[] for x in range(m+1)]

    #진입차수
    ind = [0 for x in range(m+1)]

    # n번째 노드의 (최대값, 개수)
    check = [[0, 0] for x in range(m+1)]

    q = deque()

    for x in range(p):
        a, b = map(int, input().split())
        table[a].append(b)
        ind[b] += 1

    for x in range(1, m+1):
        if ind[x] == 0:
            check[x] = [1, 1]
            q.append(x)

    while q:
        here = q.popleft()

        if check[here][1] > 1:
            check[here][0] = check[here][0] + 1
            check[here][1] = 1
        else:
            check[here][0] = check[here][0]
            check[here][1] = 1

        for there in table[here]:
            ind[there] -= 1
            if check[there][0] == check[here][0]:
                check[there][1] += 1
            elif check[there][0] < check[here][0]:
                check[there][0] = check[here][0]
                check[there][1] = 1

            if ind[there] == 0:
                q.append(there)

    print(k, check[m][0])
