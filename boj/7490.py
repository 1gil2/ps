#gold 5

import sys
input = sys.stdin.readline


def calc(st):
    st = st.replace(" ", "")
    return eval(st)


def dfs(idx):
    global st

    st += str(num[idx])
    idx += 1

    if idx == n:
        if calc(st) == 0:
            print(st)
        return

    st += ' '
    dfs(idx)
    st = st[:-2]

    st += '+'
    dfs(idx)
    st = st[:-2]

    st += '-'
    dfs(idx)
    st = st[:-2]


t = int(input())

for _ in range(t - 1):
    n = int(input())
    num = [x + 1 for x in range(n)]

    st = ''
    dfs(0)
    print()

n = int(input())
num = [x + 1 for x in range(n)]

st = ''
dfs(0)
