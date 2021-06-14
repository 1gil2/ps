#gold 3

import sys

input = sys.stdin.readline


def galho(st):
    if st[2] == '+':
        return int(st[1]) + int(st[3])
    if st[2] == '-':
        return int(st[1]) - int(st[3])
    if st[2] == '*':
        return int(st[1]) * int(st[3])


def calc(st):
    idx = 0
    le = len(st)
    op = '+'
    ret = 0
    while idx < le:
        if st[idx].isdigit():
            if op == '+':
                ret += int(st[idx])
            elif op == '-':
                ret -= int(st[idx])
            elif op == '*':
                ret *= int(st[idx])
            idx += 1
            continue

        if st[idx] == '(':
            temp = galho(st[idx:idx + 5])
            if op == '+':
                ret += temp
            elif op == '-':
                ret -= temp
            elif op == '*':
                ret *= temp
            idx += 5
            continue

        if st[idx] == '+' or st[idx] == '-' or st[idx] == '*':
            op = st[idx]
            idx += 1
            continue

    return ret


def dfs(st, idx, flag):
    global ans

    if idx == n:
        if flag:
            ans = max(ans, calc(st))
            return
        else:
            ans = max(ans, calc(st + ')'))
            return

    if cmd[idx].isdigit():
        if flag:
            dfs(st + cmd[idx], idx + 1, flag)
            if idx < n - 1:
                dfs(st + '(' + cmd[idx], idx + 1, False)
        else:
            dfs(st + cmd[idx] + ')', idx + 1, True)

    else:
        dfs(st + cmd[idx], idx + 1, flag)


n = int(input())
cmd = input().rstrip()
ans = -sys.maxsize

dfs('', 0, True)

print(ans)
