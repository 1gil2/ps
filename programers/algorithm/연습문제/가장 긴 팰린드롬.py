#level 3


def check(st):
    for x in range(len(st) // 2 + 1):
        if st[x] != st[-x - 1]:
            return False
    return True


def solution(s):
    ls = len(s)
    for cut in range(ls, 1, -1):
        for idx in range(ls - cut + 1):
            if check(s[idx:idx + cut]):
                return cut

    return 1
