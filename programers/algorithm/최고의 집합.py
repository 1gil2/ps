#level 3


def solution(n, s):
    if n > s:
        return [-1]

    mok = s // n
    mod = s % n

    answer = []
    for x in range(n - mod):
        answer.append(mok)
    for x in range(mod):
        answer.append(mok + 1)

    return answer
