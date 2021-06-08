#gold 2

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(idx):
    ret = table[idx][0]

    for x in table[idx][1]:
        ret += dfs(x)

    if ret < 0:
        return 0
    return ret


n = int(input())
table = [[0, []] for x in range(n + 1)]

for x in range(2, n + 1):
    animal, many, vec = input().split()

    if animal == 'W':
        many = -int(many)
    else:
        many = int(many)

    table[x][0] = many
    table[int(vec)][1].append(x)

print(dfs(1))
