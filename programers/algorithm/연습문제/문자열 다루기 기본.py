#level 1


def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False

    return answer and s.isdigit()
