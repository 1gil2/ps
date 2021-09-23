#level 1


def solution(strings, n):
    new_strings = []
    for st in strings:
        new_strings.append(st[n] + st)
    new_strings.sort()
    answer = []
    for st in new_strings:
        answer.append(st[1:])

    return answer
