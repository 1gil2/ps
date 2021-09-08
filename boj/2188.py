#platinum 4

import sys

input = sys.stdin.readline


def dfs(cow):
    visit[cow] = True

    for barn in table[cow]:
        if barns[barn] == -1 or (not visit[barns[barn]] and dfs(barns[barn])):
            cows[cow] = barn
            barns[barn] = cow
            return True

    return False


n, m = map(int, input().split())

table = [[] for x in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    s = temp[0]
    arr = temp[1:]

    for j in range(s):
        table[i].append(arr[j])

ans = 0
cows = [-1 for x in range(n + 1)]
barns = [-1 for x in range(m + 1)]

for x in range(1, n + 1):
    if cows[x] == -1:
        visit = [False for x in range(n + 1)]
        if dfs(x):
            ans += 1

print(ans)
