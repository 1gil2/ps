#level 1


def solution(s):
    cnt = 0

    for c in s:
        if c == 'P' or c == 'p':
            cnt += 1
        elif c == 'Y' or c == 'y':
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False