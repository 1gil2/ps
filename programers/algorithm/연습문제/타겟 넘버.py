#level 2


def solution(numbers, target):
    answer = [0]
    for x in numbers:
        temp = []
        for y in answer:
            temp.append(y+x)
            temp.append(y-x)
        answer = temp
    return answer.count(target)
