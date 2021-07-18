#gold 4

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def dfs(idx, temp):
    global ans

    if idx == 11:
        ans = max(ans, temp)
        return

    for i, lv in enumerate(table[idx]):
        if lv != 0 and visit[i] == 0:
            visit[i] = 1
            dfs(idx + 1, temp + lv)
            visit[i] = 0


t = int(input())
for _ in range(t):
    table = []
    for x in range(11):
        table.append(list(map(int, input().split())))

    visit = [0 for x in range(11)]
    ans = 0

    dfs(0, 0)

    print(ans)
