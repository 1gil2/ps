#gold 4

import sys

input = sys.stdin.readline


def dfs(idx, deep):
    if le == deep:
        print(''.join(answer))
        return

    for x in range(26):
        if alpha[x]:
            alpha[x] -= 1
            answer[deep] = chr(97 + x)
            dfs(x, deep + 1)
            alpha[x] += 1


n = int(input())
for _ in range(n):
    st = list(input().rstrip())
    le = len(st)

    answer = [' ' for x in range(le)]

    alpha = [0 for x in range(26)]
    for s in st:
        alpha[ord(s) - 97] += 1

    dfs(0, 0)
