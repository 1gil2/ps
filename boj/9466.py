#gold 3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(here):
    global answer
    visit[here] = 1
    trace.append(here)

    there = table[here]
    if visit[there]:
        if there in trace:
            answer += trace[trace.index(there):]
        return
    else:
        dfs(there)


t = int(input())
for _ in range(t):
    n = int(input())
    table = [0] + list(map(int, input().split()))

    visit = [0 for x in range(n + 1)]
    answer = []

    for x in range(1, n + 1):
        if not visit[x]:
            trace = []
            dfs(x)

    print(n - len(answer))
