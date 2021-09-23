#level 2


def solution(n):
    answer = ''
    share = n

    while share != 0:
        temp = share % 3
        share //= 3

        if temp == 0:
            answer = '4' + answer
            share -= 1
        elif temp == 1:
            answer = '1' + answer
        elif temp == 2:
            answer = '2' + answer

    return answer
