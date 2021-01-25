#gold 3

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

cost = [0 for x in range(n+1)]
before = [[] for x in range(n+1)] #i가 지어지면 지을수 있는 건물
indegree = [0 for x in range(n+1)] #진입차수
ans = [0 for x in range(n+1)] #하위건물까지 고려했을때의 시간

dq = deque()
for x in range(1, n+1):
    temp = list(map(int, input().split()))
    cost[x] = temp[0]
    for y in range(1, len(temp)):
        if temp[y] == -1:
            break
        else:
            before[temp[y]].append(x)
            indegree[x] += 1

for x in range(1, n+1):
    if indegree[x] == 0:
        ans[x] = cost[x]
        dq.append(x)

for x in range(1, n+1):
    cur = dq.popleft()
    for nxt in before[cur]:
        ans[nxt] = max(ans[nxt], ans[cur]+cost[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            dq.append(nxt)

for x in range(1, n+1):
    print(ans[x])
