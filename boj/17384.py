#platinum 5
#pypy3

import sys

input = sys.stdin.readline
inf = sys.maxsize


def vs(s, e, team):
    if s == e:
        if team:
            print('#', end='')
        else:
            print('.', end='')
        return

    m = (s + e) // 2

    half = (e - s + 1) // 2
    qurt = half // 2

    if team > half:
        t1 = team - qurt
        t2 = qurt
        if t1 > half:
            t1 = half
            t2 = team - half
        vs(s, m, t1)
        vs(m + 1, e, t2)
    else:
        vs(s, m, team)
        vs(m + 1, e, 0)


n = int(input())
nn = (n - 1).bit_length()
size = 1 << nn

vs(1, size, n)
