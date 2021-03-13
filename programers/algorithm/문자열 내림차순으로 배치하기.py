#level 1


def solution(s):
    answer = []
    for x in s:
        answer.append(x)
    answer.sort(reverse=True)

    return ''.join(answer)
