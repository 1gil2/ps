#gold 5

import sys
input = sys.stdin.readline


def dfs(num):
    for i in range(2, int(int(num) ** 0.5) + 1):
        if int(num) % i == 0:
            return

    if len(num) == n:
        print(num)
        return

    for p in prime:
        dfs(num + p)


n = int(input())
num = ['2', '3', '5', '7']

prime = ['1', '3', '7', '9']

for x in num:
    dfs(x)
