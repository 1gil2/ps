#gold 4

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def check(st):
    ls = len(st)

    for s in range(ls):
        for gap in range(1, ls // 2 + 1):

            idx = s

            while idx + gap < ls:
                st1 = st[idx: idx + gap]
                st2 = st[idx + gap: idx + gap + gap]

                if st1 == st2:
                    return False

                idx += gap

    return True


def dfs(st, length):
    if length == n:
        print(st)
        sys.exit()

    for x in range(1, 4):
        new_st = st + str(x)

        if check(new_st):
            dfs(new_st, length + 1)


n = int(input())

dfs("", 0)
