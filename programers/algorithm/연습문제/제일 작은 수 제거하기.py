#level 1


def solution(arr):
    m = min(arr)
    answer = []
    for x in arr:
        if x == m:
            continue
        else:
            answer.append(x)

    if answer:
        return answer
    else:
        return [-1]
