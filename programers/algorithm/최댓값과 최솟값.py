#level 2


def solution(s):
    L = list(map(int, s.split(' ')))
    M = max(L)
    m = min(L)
    return str(m) + ' ' + str(M)
