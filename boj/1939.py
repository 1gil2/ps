#gold 4

import sys
from collections import deque

input = sys.stdin.readline


def bfs(weight):
    dq = deque()
    dq.append(start)
    visit = [0 for x in range(n + 1)]
    visit[start] = 1

    while dq:
        here = dq.popleft()

        if here == end:
            return True

        for there, cost in table[here]:
            if visit[there] == 0 and weight <= cost:
                visit[there] = 1
                dq.append(there)

    return False


n, m = map(int, input().split())

table = [[] for x in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    table[a].append((b, c))
    table[b].append((a, c))

start, end = map(int, input().split())

left = 0
right = 1000000000
ans = 0

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
