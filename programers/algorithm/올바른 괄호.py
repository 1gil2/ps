#level 2


def solution(s):
    cnt = 0

    for x in s:
        if x == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1

    if cnt == 0:
        return True
    return False
