#level 1


def solution(x):
    n = 0
    for y in str(x):
        n += int(y)

    if x % n == 0:
        return True
    else:
        return False
