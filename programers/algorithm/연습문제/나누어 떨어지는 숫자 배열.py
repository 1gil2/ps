#level 1


def solution(arr, divisor):
    answer = []
    for n in arr:
        if n % divisor == 0:
            answer.append(n)

    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer
