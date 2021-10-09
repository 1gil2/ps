#level 4


def solution(begin, end):
    answer = []

    for x in range(begin, end + 1):
        if x == 1:
            answer.append(0)
        else:
            sqrt = int(x ** 0.5)
            for y in range(2, sqrt + 1):
                if x % y == 0 and x // y <= 10 ** 7:
                    answer.append(x // y)
                    break
            else:
                answer.append(1)

    return answer
