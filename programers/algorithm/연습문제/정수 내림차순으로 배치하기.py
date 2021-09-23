#level 1


def solution(n):
    a = []
    for x in str(n):
        a.append(x)
    a.sort(reverse=True)
    return int(''.join(a))
