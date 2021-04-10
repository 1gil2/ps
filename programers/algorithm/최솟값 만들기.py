#level 2


def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for idx, a in enumerate(A):
        answer += a*B[-idx-1]

    return answer
