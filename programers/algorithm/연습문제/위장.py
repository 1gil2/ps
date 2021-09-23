#level 2


def solution(clothes):
    D = dict()

    for val, key in clothes:
        try:
            D[key] += 1
        except:
            D[key] = 1

    answer = 1
    for x in D.values():
        answer *= x + 1

    return answer - 1
