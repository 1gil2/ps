#level 1


def solution(d, budget):
    d.sort()
    answer = 0

    money = 0
    for x in d:
        money += x
        answer += 1
        if money > budget:
            answer -= 1
            break

    return answer
