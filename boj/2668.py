#gold 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(node, start):
    nxt = nums[node]

    if nxt == start:
        answer.append(nxt)

    if visit[nxt] == 0:
        visit[nxt] = 1
        dfs(nxt, start)


n = int(input())
nums = [0] + [int(input()) for x in range(n)]

answer = []
for x in range(1, n + 1):
    visit = [0 for _ in range(n + 1)]
    visit[x] = 1
    dfs(x, x)

print(len(answer))
answer.sort()
for x in answer:
    print(x)
